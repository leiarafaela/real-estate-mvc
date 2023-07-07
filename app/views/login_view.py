from app import app
from flask import request, jsonify
from ..controllers.login_controller import create_token, logout, create_access_token


@app.route('/login/token', methods=['POST'])
def view_create_token():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    return create_token(email, password)

@app.route('/logout', methods=['POST'])
def view_logout():
    logout
    return jsonify({'msg': 'logout successful!'})
