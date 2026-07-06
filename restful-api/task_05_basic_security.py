#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret-key"

jwt = JWTManager(app)

auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },

    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify(username, password):

    if username in users:

        if check_password_hash(users[username]["password"], password):
            return username

    return None


@app.route("/basic-protected")
@auth.login_required
def basic():

    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")

    password = data.get("password")

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=username)

    return jsonify(access_token=token)


@app.route("/jwt-protected")
@jwt_required()
def jwt_route():

    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin():

    username = get_jwt_identity()

    if users[username]["role"] != "admin":

        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


@jwt.unauthorized_loader
def unauthorized(e):

    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid(e):

    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired(a, b):

    return jsonify({"error": "Token has expired"}), 401


if __name__ == "__main__":

    app.run()
