from app.api import bp
from app import db, bcrypt
from flask import request, make_response, jsonify
from app.models import User, BlacklistToken


@bp.route("/auth/login", methods=["POST"])
def login():
    post_data = request.get_json()
    try:
        user = User.query.filter_by(email=post_data.get("email")).first()
        if user and bcrypt.check_password_hash(
            user.password, post_data.get("password")
        ):
            auth_token = user.encode_auth_token(user.id)
            if auth_token:
                responseObject = {
                    "status": "success",
                    "message": "Successfully logged in.",
                    "auth_token": auth_token.decode(),
                }
                return make_response(jsonify(responseObject)), 200
        else:
            responseObject = {"status": "fail", "message": "User does not exist."}
            return make_response(jsonify(responseObject)), 404
    except Exception as e:
        print(e)
        responseObject = {"status": "fail", "message": "Try again"}
        return make_response(jsonify(responseObject)), 500


@bp.route("/auth/logout", methods=["POST"])
def logout():
    # get auth token
    auth_header = request.headers.get("Authorization")
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ""
    if auth_token:
        resp = User.decode_auth_token(auth_token)
        if not isinstance(resp, str):
            # mark the token as blacklisted
            blacklist_token = BlacklistToken(token=auth_token)
            try:
                # insert the token
                db.session.add(blacklist_token)
                db.session.commit()
                responseObject = {
                    "status": "success",
                    "message": "Successfully logged out.",
                }
                return make_response(jsonify(responseObject)), 200
            except Exception as e:
                responseObject = {"status": "fail", "message": e}
                return make_response(jsonify(responseObject)), 200
        else:
            responseObject = {"status": "fail", "message": resp}
            return make_response(jsonify(responseObject)), 401
    else:
        responseObject = {"status": "fail", "message": "Provide a valid auth token."}
        return make_response(jsonify(responseObject)), 403
