import mercadopago

def payment(value):
    valueInt = int(value)
    preference = {
        "items": [
        {
            "title": "Shopping Cart",
            "quantity": 1,
            "currency_id": "BRL",
            "unit_price": valueInt
            
            }
        ]
    }

    mp = mercadopago.SDK("TEST-7928821890491680-051819-916f654b800320fa3af09cd19824117c-479481641")

    preferenceResult = mp.preference().create(preference)

    url = preferenceResult["response"]["init_point"]
    
    return url
    
