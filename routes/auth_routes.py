from flask import Blueprint, request, render_template, redirect
from flask_jwt_extended import create_access_token
from models.user_model import User
from extensions import db

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

# REGISTER
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        user = User(
            name=name,
            email=email,
            password=password,
            role=role
        )

        db.session.add(user)
        db.session.commit()

        return redirect('/dashboard')

    return render_template('register.html')