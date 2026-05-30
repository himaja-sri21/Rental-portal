from flask import Blueprint, request, render_template, redirect
from flask_jwt_extended import create_access_token
from models.user_model import User

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and user.password == password:

            token = create_access_token(identity=user.email)

            print("JWT Token:", token)

            return redirect('/dashboard')

        return "Invalid email or password"

    return render_template('login.html')