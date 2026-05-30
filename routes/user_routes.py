# =========================
# routes/user_routes.py
# =========================

from flask import Blueprint, request, jsonify
from extensions import db
from models.user_model import User

user_bp = Blueprint('user_bp', __name__)

# CREATE USER
@user_bp.route('/users', methods=['POST'])
def create_user():
    """
    Create User
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          properties:
            name:
              type: string
            email:
              type: string
            password:
              type: string
            role:
              type: string

    responses:
      200:
        description: User created successfully
    """

    data = request.json

    user = User(
        name=data['name'],
        email=data['email'],
        password=data['password'],
        role=data['role']
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User created successfully"
    })


# GET USERS
@user_bp.route('/users', methods=['GET'])
def get_users():
    """
    Get All Users
    ---
    responses:
      200:
        description: List of users
    """

    users = User.query.all()

    result = []

    for user in users:
        result.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        })

    return jsonify(result)


# UPDATE USER
@user_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    """
    Update User
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true

    responses:
      200:
        description: User updated successfully
    """

    user = User.query.get(id)

    if not user:
        return jsonify({
            "message": "User not found"
        }), 404

    data = request.json

    user.name = data['name']
    user.email = data['email']
    user.password = data['password']
    user.role = data['role']

    db.session.commit()

    return jsonify({
        "message": "User updated successfully"
    })


# DELETE USER
@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    """
    Delete User
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true

    responses:
      200:
        description: User deleted successfully
    """

    user = User.query.get(id)

    if not user:
        return jsonify({
            "message": "User not found"
        }), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({
        "message": "User deleted successfully"
    })