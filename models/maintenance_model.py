from extensions import db

class Maintenance(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    tenant_name = db.Column(db.String(100))

    issue = db.Column(db.String(300))

    status = db.Column(db.String(50))