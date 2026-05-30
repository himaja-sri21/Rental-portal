from models.user_model import User
from extensions import db


# CREATE USER

def create_user_service(data):

    user = User(
        name=data['name'],
        email=data['email'],
        password=data['password'],
        role=data['role']
    )

    db.session.add(user)
    db.session.commit()

    return {
        "message": "User created successfully"
    }


# GET USERS

def get_users_service():

    users = User.query.all()

    result = []

    for user in users:

        result.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        })

    return result


# UPDATE USER

def update_user_service(id, data):

    user = User.query.get(id)

    if not user:

        return {
            "message": "User not found"
        }

    user.name = data['name']
    user.email = data['email']
    user.password = data['password']
    user.role = data['role']

    db.session.commit()

    return {
        "message": "User updated successfully"
    }


# DELETE USER

def delete_user_service(id):

    user = User.query.get(id)

    if not user:

        return {
            "message": "User not found"
        }

    db.session.delete(user)
    db.session.commit()

    return {
        "message": "User deleted successfully"
    }