"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
import stripe

api = Blueprint('api', __name__)
stripe.api_key = 'sk_test_51LTCnvA9wzTLXCek9Xh0wo8hUCyEDMVVFehIuRAOwSThanw6MQ1c05QtWG9dGkbg15Cc9IUmlkI7gUSWYXjhCyAt00S48LJLUp'

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200



@api.route('/create-payment', methods=['POST'])
def create_payment():
    try:
        data = request.json
        intent = stripe.PaymentIntent.create(
            amount=data['amount'],
            currency=data['currency'],
            automatic_payment_methods={
                'enabled': True
            }

        )
        return jsonify({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

