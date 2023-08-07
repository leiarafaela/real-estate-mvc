from app.config.connect import db
from flask_cors import CORS

from app import app
from app.views import login_view, user_view, mercado_pago_view


CORS(app, supports_credentials=True)
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    