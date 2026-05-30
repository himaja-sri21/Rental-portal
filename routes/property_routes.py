# =========================
# routes/property_routes.py
# =========================

from flask import Blueprint, request, jsonify
from extensions import db
from models.property_model import Property

property_bp = Blueprint('property_bp', __name__)


# CREATE PROPERTY
@property_bp.route('/properties', methods=['POST'])
def create_property():
    """
    Create Property
    ---
    responses:
      200:
        description: Property created
    """

    data = request.json

    property = Property(
        title=data['title'],
        location=data['location'],
        price=data['price']
    )

    db.session.add(property)
    db.session.commit()

    return jsonify({
        "message": "Property created successfully"
    })


# GET PROPERTIES
@property_bp.route('/properties', methods=['GET'])
def get_properties():
    """
    Get Properties
    ---
    responses:
      200:
        description: List of properties
    """

    properties = Property.query.all()

    result = []

    for property in properties:
        result.append({
            "id": property.id,
            "title": property.title,
            "location": property.location,
            "price": property.price
        })

    return jsonify(result)