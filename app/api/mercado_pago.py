import mercadopago
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN=os.getenv('TOKEN_TEST')

def payment(value):
    preference = {
        "items": [
        {
            "title": "Shopping Cart",
            "quantity": 1,
            "currency_id": "BRL",
            "unit_price": value
            
            }
        ]
    }

    mp = mercadopago.SDK(TOKEN)

    preferenceResult = mp.preference().create(preference)
    return preferenceResult   