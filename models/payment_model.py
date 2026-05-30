from extensions import db

class Payment(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    tenant_name = db.Column(db.String(100))

    amount = db.Column(db.Float)

    payment_date = db.Column(db.String(50))

    status = db.Column(db.String(50))