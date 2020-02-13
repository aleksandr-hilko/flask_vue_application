from app.api import bp
from app import db
from app.api.serializers import project_schema, projects_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Project
import os
from flask import current_app as app
import random


@bp.route("/projects/<int:pk>/upload_contract", methods=["POST"])
def upload_contract(pk):
    """ Upload file and set project name as the uploaded file path. """
    if "file" in request.files:
        project = Project.query.get_or_404(pk)
        file_ = request.files["file"]
        file_extension = file_.filename.split(".")[-1]
        filename = f"{project.name}.{file_extension}"
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file_.save(file_path)
        project.contract = file_path
        db.session.commit()
        return "File is uploaded successfully"
    else:
        return {"message": "No file is provided"}, 400


@bp.route("/projects", methods=["POST"])
def create_project():
    import pdb

    pdb.set_trace()
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
def get_projects():
    projects = Project.query.all()
    projects = projects_schema.dump(projects, many=True)
    return jsonify(projects)


@bp.route("/projects/<int:pk>", methods=["GET"])
def get_project(pk):
    project = Project.query.get_or_404(pk)
    project = project_schema.dump(project)
    return jsonify(project)


@bp.route("/projects/<int:pk>", methods=["PUT"])
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
def delete_project(pk):
    project = Project.query.get_or_404(pk)
    db.session.delete(project)
    db.session.commit()
    return "", 204
