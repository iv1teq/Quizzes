from flask import Blueprint, request
import os
import json

New_Quiz = Blueprint(
    "New_Quiz",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/new_quiz",

)

import flask,os


DIR=os.path.abspath(os.path.dirname(__file__))

join = flask.Blueprint(
    name= "join",
    import_name = "join",
    template_folder='templates',
    static_folder=os.path.join(DIR, "static"),
    static_url_path="/join"
)

DATA_FOLDER = os.path.join(os.path.dirname(__file__), "static", "quiz_data")
os.makedirs(DATA_FOLDER, exist_ok=True)
DATA_FILE = os.path.join(DATA_FOLDER, "quiz_data.json")

def save_quiz():
    new_data = request.get_json()
    
    quiz_name = new_data.get('quiz_name')
    if not quiz_name:
        return {'status': 'error', 'message': 'Quiz name not provided'}, 400

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            try:
                quiz_data = json.load(file)
            except:
                quiz_data = {}
    else:
        quiz_data = {}

    if not isinstance(quiz_data, dict):
        quiz_data = {}

    if quiz_name not in quiz_data:
        quiz_data[quiz_name] = {
            'name': quiz_name,
            'topic': new_data.get('topic', ''),
            'questions': []
        }

    question_data = {
        'mode': new_data.get('mode'),
        'question': new_data.get('question'),
        'answers': new_data.get('answers', [])
    }
    quiz_data[quiz_name]['questions'].append(question_data)

    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(quiz_data, file, ensure_ascii=False, indent=2)

    return {'status': 'success'}