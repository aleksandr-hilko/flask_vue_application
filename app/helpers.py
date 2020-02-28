import os
from flask import request, make_response, jsonify
from functools import wraps


def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


def check_token(f):
    """
    Wrapper around view to verify that valid token is provided with request.
    """
    from app.models import User
    from flask import g

    @wraps(f)
    def decorated(*args, **kwargs):
        # get the auth token
        auth_header = request.headers.get("Authorization")
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ""
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                g.current_user = user

                return f(*args, **kwargs)

            responseObject = {"status": "fail", "message": resp}
            return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                "status": "fail",
                "message": "Provide a valid auth token.",
            }
            return make_response(jsonify(responseObject)), 401

    return decorated
