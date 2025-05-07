import os
import json
from flask import Blueprint, request, jsonify

DIR = os.path.dirname(os.path.abspath(__file__))

New_Quiz = Blueprint(
    "New_Quiz",
    __name__,
    template_folder="templates",
    static_folder=os.path.join(DIR, 'static'),
    static_url_path="/new_quiz",

)

QUIZ_SAVE_DIR = os.path.join(DIR, 'static', 'quiz_data')

os.makedirs(QUIZ_SAVE_DIR, exist_ok=True)

@New_Quiz.route('/save_quiz', methods=['POST'])
def save_quiz():
    data = request.get_json()
    save_path = os.path.join(QUIZ_SAVE_DIR, 'quiz_data.json')
    with open(save_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        

  
