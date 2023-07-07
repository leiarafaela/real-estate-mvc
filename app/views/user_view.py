from flask import request
from flask_jwt_extended import jwt_required

from app import app
from ..controllers.user_controller import signup, my_profile


@app.route('/')
def home():
    return '<h1>ola <h1/>'

@app.route('/signup', methods=['POST'])
def view_signup():
    user = request.json
    return signup(user)

@app.route('/profile/<getemail>', methods=['GET'])
@jwt_required()
def view_my_profile(getemail):
    return my_profile(getemail)
