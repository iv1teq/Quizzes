from project.settings import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(30), nullable = False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        return f"name: {self.name}, is_admin: {self.is_admin}"