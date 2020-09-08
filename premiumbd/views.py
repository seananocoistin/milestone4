import json
import stripe
# This is your real test secret API key.
stripe.api_key = "sk_test_51HOPTbISk250XzF1E4wXttTqznsQ8Uw5ADXxsyHu9PbuvvfMk2a6T3AYMCrcReC2dHP2kCIybSBkzuodf89ONbk000yLRnISsE"

def create_payment():
    try:
        data = json.loads(request.data)
        intent = stripe.PaymentIntent.create(
            amount=calculate_order_amount(data['items']),
            currency='eur'
        )
        return json.dumps({
          'clientSecret': intent['client_secret']
        })
    except: