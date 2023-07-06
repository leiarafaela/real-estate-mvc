import json
from app import app
from flask import request, jsonify
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, unset_jwt_cookies, JWTManager
from flask_bcrypt import Bcrypt

from ..models.user import User

app.config['SECRET_KEY'] = 'rafaelaaugusto-teste'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=2)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)


@app.route('/logintoken', methods=['POST'])
def create_token():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    user = User.query.filter_by(email=email).first()
    if user is None:
        return jsonify({"msg": "email ou senha errados"}), 401
    
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Nao autorizado"}), 401
    
    access_token = create_access_token(identity=email)
    # response= {"access_token": access_token}

    return jsonify({
        "email": email,
        "access_token": access_token
    })

@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()['exp']
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data['access_token'] = access_token
                response.data = json.dump(data)
        return response

    except (RuntimeError, KeyError):
        return response

@app.route('/logout', methods=['POST'])
def logout():
    response = jsonify({'msg': 'logout successful!'})
    unset_jwt_cookies(response)
    return response

