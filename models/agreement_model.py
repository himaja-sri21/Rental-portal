from extensions import db

class Agreement(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    tenant_name = db.Column(db.String(100))

    property_address = db.Column(db.String(200))

    start_date = db.Column(db.String(50))

    end_date = db.Column(db.String(50))

    document_url = db.Column(db.String(300))