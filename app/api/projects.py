from app.api import bp
from app import db
from app.api.serializers import project_schema, projects_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Project, Customer
import os
from flask import current_app as app
import random
import tempfile
from sqlalchemy import desc, asc
from drive import upload_to_google_drive
from app.helpers import check_token


@bp.route("/projects/<int:pk>/upload_contract", methods=["POST"])
@check_token
def upload_contract(pk):
    """ Upload file to google drive and 
        set project model contract field to the link to the uploaded file. """
    if "file" in request.files:
        project = Project.query.get_or_404(pk)
        file_ = request.files["file"]
        filename = project.name
        with tempfile.TemporaryDirectory() as tmpdirname:
            file_path = os.path.join(tmpdirname, filename)
            file_.save(file_path)

            try:
                drive_file = upload_to_google_drive(file_path, filename, file_.mimetype)
            except Exception as e:
                return {"message": f"Failed to upload: {e}"}, 400
            project.contract = drive_file["alternateLink"]
            db.session.commit()
        return "File is uploaded successfully"
    else:
        return {"message": "No file is provided"}, 400


@bp.route("/projects", methods=["POST"])
@check_token
def create_project():
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    try:
        project = project_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 400
    # This is needed to prevent saving contract field
    # in the model without uploading the file
    project.contract = None
    db.session.add(project)
    db.session.commit()
    result = project_schema.dump(
        Project.query.filter(Project.name == project.name).first()
    )
    return jsonify(result)


@bp.route("/projects", methods=["GET"])
@check_token
def get_projects():
    params = request.args
    order_params = params.get("order")
    query = Project.query.join(Customer)
    query = filter_query(query, params)
    if order_params:
        order_column, order_dir = order_params.split(":")
        order = asc(order_column) if order_dir == "asc" else desc(order_column)
        projects = query.order_by(order).all()
    else:
        projects = query.all()
    projects = projects_schema.dump(projects, many=True)
    return jsonify(projects)


def filter_query(query, params):
    work_started = params.get("work_started")
    has_plan = params.get("has_plan")
    has_contract = params.get("has_contract")
    min_price = params.get("min_price")
    max_price = params.get("max_price")
    customer_name = params.get("customer_name")

    if work_started:
        query = query.filter(Project.work_started == True)
    if has_plan:
        query = query.filter(Project.has_plan == True)
    if has_contract:
        query = query.filter(Project.has_contract == True)
    if customer_name:
        query = query.filter(Customer.customer_name == customer_name)

    return query


@bp.route("/projects/<int:pk>", methods=["GET"])
@check_token
def get_project(pk):
    project = Project.query.get_or_404(pk)
    project = project_schema.dump(project)
    return jsonify(project)


@bp.route("/projects/<int:pk>", methods=["PUT"])
@check_token
def update_project(pk):
    project = Project.query.get_or_404(pk)
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    errors = project_schema.validate(json_data, partial=True, session=db.session)
    if errors:
        return errors, 400
    project.update(**json_data)
    db.session.commit()
    result = project_schema.dump(project)
    return jsonify(result), 201


@bp.route("/projects/<int:pk>", methods=["DELETE"])
@check_token
def delete_project(pk):
    project = Project.query.get_or_404(pk)
    db.session.delete(project)
    db.session.commit()
    return "", 204
