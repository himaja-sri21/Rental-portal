from flask import Flask
from flasgger import Swagger
from extensions import db
from routes.property_routes import property_bp
from models.property_model import Property
from models.agreement_model import Agreement
from routes.agreement_routes import agreement_bp
from models.payment_model import Payment
from routes.payment_routes import payment_bp
from models.maintenance_model import Maintenance
from routes.maintenance_routes import maintenance_bp
from flask_jwt_extended import JWTManager
from routes.auth_routes import auth_bp
from flask import render_template
from models.user_model import User
from models.property_model import Property
from models.payment_model import Payment
from models.agreement_model import Agreement
from models.maintenance_model import Maintenance

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
jwt = JWTManager(app)

swagger = Swagger(app)

from routes.user_routes import user_bp

app.register_blueprint(user_bp)
app.register_blueprint(property_bp)
app.register_blueprint(agreement_bp)
app.register_blueprint(payment_bp)
app.register_blueprint(maintenance_bp)
app.register_blueprint(auth_bp)

from flask import render_template


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/login')
def login_page():

    return render_template('login.html')


@app.route('/register')
def register_page():

    return render_template('register.html')


@app.route('/dashboard')
def dashboard_page():

    total_properties = Property.query.count()

    total_tenants = User.query.filter_by(role='tenant').count()

    return render_template(
        'dashboard.html',
        total_properties=total_properties,
        total_tenants=total_tenants
    )
    
@app.route('/payments-page')
def payments_page():

    payments = Payment.query.all()

    return render_template(
        'payments.html',
        payments=payments
    )


@app.route('/agreements-page')
def agreements_page():

    agreements = Agreement.query.all()

    return render_template(
        'agreements.html',
        agreements=agreements
    )


@app.route('/maintenance-page')
def maintenance_page():

    maintenances = Maintenance.query.all()

    return render_template(
        'maintenance.html',
        maintenances=maintenances
    )


@app.route('/tenants-page')
def tenants_page():

    tenants = User.query.filter_by(role='tenant').all()

    return render_template(
        'tenants.html',
        tenants=tenants
    )

@app.route('/landlords-page')
def landlords_page():

    landlords = User.query.filter_by(role='landlord').all()

    return render_template(
        'landlords.html',
        landlords=landlords
    )

    
if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)
    