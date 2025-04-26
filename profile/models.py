from project.settings import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    is_admin = db.Column(db.String(30), nullable=False, default='Student')

    def __repr__(self) -> str:
        return f"name: {self.name}, email: {self.email}, is_admin: {self.is_admin}"
