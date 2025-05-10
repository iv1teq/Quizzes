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



DATA_FOLDER = os.path.join(os.path.dirname(__file__), "static", "quiz_data")
os.makedirs(DATA_FOLDER, exist_ok=True)
DATA_FILE = os.path.join(DATA_FOLDER, "quiz_data.json")

def save_quiz():
    
    new_data = request.get_json()

  
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            try:
                old_data = json.load(file)
            except:
                old_data = []
    else:
        old_data = []

   
    if not isinstance(old_data, list):
        old_data = []


    old_data.append(new_data)


    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(old_data, file, ensure_ascii=False, indent=2)

    return {'status': 'success'}