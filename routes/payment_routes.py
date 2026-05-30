from flask import Blueprint, request, jsonify
from extensions import db
from models.payment_model import Payment
import razorpay

payment_bp = Blueprint('payment_bp', __name__)

# Razorpay Client
client = razorpay.Client(
    auth=(
        "rzp_test_SvRGY0AJxh6Det",
        "dx0EAcs7keZ6Qa2DIonSUd57"
    )
)

from flask import request, jsonify

@payment_bp.route('/create-order', methods=['POST'])
def create_order():
    """
    Create Razorpay Order
    ---
    parameters:
      - in: body
        name: body
        schema:
          properties:
            amount:
              type: integer
    responses:
      200:
        description: Razorpay Order Created
    """

    try:
        data = request.json

        amount = int(data['amount']) * 100

        order = client.order.create({
            "amount": amount,
            "currency": "INR"
        })

        return jsonify(order)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@payment_bp.route('/payments', methods=['POST'])
def create_payment():

    data = request.json

    payment = Payment(
        amount=data['amount'],
        status=data['status']
    )

    db.session.add(payment)
    db.session.commit()

    return jsonify({
        "message": "Payment added successfully"
    })



@payment_bp.route('/payments', methods=['GET'])
def get_payments():
    """
    Get Payments
    ---
    responses:
      200:
        description: List of payments
    """

    payments = Payment.query.all()

    result = []

    for payment in payments:
        result.append({
            "id": payment.id,
            "amount": payment.amount,
            "status": payment.status
        })

    return jsonify(result)


@payment_bp.route('/payments/<int:id>', methods=['PUT'])
def update_payment(id):

    payment = Payment.query.get(id)

    if not payment:
        return jsonify({
            "message": "Payment not found"
        }), 404

    data = request.json

    payment.amount = data['amount']
    payment.status = data['status']

    db.session.commit()

    return jsonify({
        "message": "Payment updated successfully"
    })


@payment_bp.route('/payments/<int:id>', methods=['DELETE'])
def delete_payment(id):

    payment = Payment.query.get(id)

    if not payment:
        return jsonify({
            "message": "Payment not found"
        }), 404

    db.session.delete(payment)
    db.session.commit()

    return jsonify({
        "message": "Payment deleted successfully"
    })