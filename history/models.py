from project.settings import db

class QuizzesHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    history_tests = db.Column(db.String(255) , nullable=False)
    date = db.Column(db.String(80), nullable=False)
    quiz_id = db.Column(db.Integer , nullable=False)