# =========================
# routes/agreement_routes.py
# =========================

from flask import Blueprint, request, jsonify
from extensions import db
from models.agreement_model import Agreement

agreement_bp = Blueprint('agreement_bp', __name__)


# CREATE AGREEMENT
@agreement_bp.route('/agreements', methods=['POST'])
def create_agreement():
    """
    Create Agreement
    ---
    responses:
      200:
        description: Agreement created
    """

    data = request.json

    agreement = Agreement(
        start_date=data['start_date'],
        end_date=data['end_date']
    )

    db.session.add(agreement)
    db.session.commit()

    return jsonify({
        "message": "Agreement created successfully"
    })


# GET AGREEMENTS
@agreement_bp.route('/agreements', methods=['GET'])
def get_agreements():
    """
    Get Agreements
    ---
    responses:
      200:
        description: List of agreements
    """

    agreements = Agreement.query.all()

    result = []

    for agreement in agreements:
        result.append({
            "id": agreement.id,
            "start_date": agreement.start_date,
            "end_date": agreement.end_date
        })

    return jsonify(result)