from flask import jsonify

from ..models.user import User


def signup(user):
    user_exists = User.query.filter_by(email=user['email']).first()

    if user_exists:
        return jsonify({"error": "user ja existente"}), 409
 
    new_user = User.create(user)

    return jsonify({
        "id": new_user.id,
        "email": new_user.email
    })

def my_profile(email):
    print(email)
    if not email:
        return jsonify({"error": "acesso negado"}), 401
    
    user = User.query.filter_by(email=email).first()

    response_body = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
    }
    
    return response_body
