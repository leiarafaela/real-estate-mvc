from app import app
from flask import request, jsonify
from flask_jwt_extended import jwt_required

from ..models.user import User

@app.route('/')
def home():
    return '<h1>ola <h1/>'


@app.route('/signup', methods=['POST'])
def signup():
    user = request.json

    user_exists = User.query.filter_by(email=user['email']).first()

    if user_exists:
        return jsonify({"error": "user ja existente"}), 409
 
    new_user = User.create(user)

    return jsonify({
        "id": new_user.id,
        "email": new_user.email
    })

@app.route('/profile/<getemail>')
@jwt_required()
def my_profile(getemail):
    print(getemail)
    if not getemail:
        return jsonify({"error": "acesso negado"}), 401
    
    user = User.query.filter_by(email=getemail).first()

    response_body = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
    }
    
    return response_body
