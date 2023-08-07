from app import app
from flask import request
from ..controllers.mercado_pago_controller import create_payment

@app.route('/mp/pagamento', methods=['POST'])
def view_payment():
    value = request.json.get('value', None)
    response = create_payment(value)
    return response