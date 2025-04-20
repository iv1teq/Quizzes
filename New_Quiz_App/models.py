from project.settings import db

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    json_test_data = db.Column(db.JSON)
    content_questions = db.Column(db.Integer, nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)

