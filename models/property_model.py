from extensions import db

class Property(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    bookings = db.relationship('Booking', backref='property', lazy=True)

    address = db.Column(db.String(200))
    rent_amount = db.Column(db.Float)
    status = db.Column(db.String(50))