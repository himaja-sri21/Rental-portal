from flask_jwt_extended import jwt_required

def token_required():

    return jwt_required()