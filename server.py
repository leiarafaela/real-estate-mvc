from app.controllers import user_controller, login_controller
from app import app
from app.config.connect import db
from flask_cors import CORS

CORS(app, supports_credentials=True)
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)