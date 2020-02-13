from app.api import bp
from app import db
from app.api.serializers import project_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Project


@bp.route("/projects", methods=["POST"])
def create_project():
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    try:
        project = project_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 400
    db.session.add(project)
    db.session.commit()
    result = project_schema.dump(
        Project.query.filter(Project.name == project.name).first()
    )
    return jsonify(result)
