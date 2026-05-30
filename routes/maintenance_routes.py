# =========================
# routes/maintenance_routes.py
# =========================

from flask import Blueprint, request, jsonify
from extensions import db
from models.maintenance_model import Maintenance

maintenance_bp = Blueprint('maintenance_bp', __name__)


# CREATE MAINTENANCE
@maintenance_bp.route('/maintenance', methods=['POST'])
def create_maintenance():
    """
    Create Maintenance Request
    ---
    responses:
      200:
        description: Maintenance request created
    """

    data = request.json

    maintenance = Maintenance(
        issue=data['issue'],
        status=data['status']
    )

    db.session.add(maintenance)
    db.session.commit()

    return jsonify({
        "message": "Maintenance request created successfully"
    })


# GET MAINTENANCE
@maintenance_bp.route('/maintenance', methods=['GET'])
def get_maintenance():
    """
    Get Maintenance Requests
    ---
    responses:
      200:
        description: List of maintenance requests
    """

    maintenances = Maintenance.query.all()

    result = []

    for maintenance in maintenances:
        result.append({
            "id": maintenance.id,
            "issue": maintenance.issue,
            "status": maintenance.status
        })

    return jsonify(result)