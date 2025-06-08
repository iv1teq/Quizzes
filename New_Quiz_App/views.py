from flask import request, render_template, redirect, url_for, session
from .models import Quiz
from project.settings import db
from flask_login import login_required, current_user
import os
import json
from flask import request, jsonify
import string

@login_required
def render_new_quiz():
    quiz_name = session.get('quiz_name') or request.args.get('quiz_name')
    if not quiz_name:
        return redirect(url_for('New_Quiz.render_new_quiz_settigs'))

    context = {
        'page': 'home',
        'is_auth': current_user.is_authenticated,
        'name': current_user.name,
        'quiz_name': quiz_name  
    }
    return render_template('New_Quiz_App.html', **context)


@login_required
def render_new_quiz_settigs():
    if not current_user.is_admin:
        return render_template('error_403.html')

    if request.method == 'POST':
        try:
            quiz_name = request.form['quiz-name']
            filename = "json_data.json"
            empty_data = []

            base_media_dir = 'media'
            os.makedirs(base_media_dir, exist_ok=True)

            quiz_folder_in_media = os.path.join(base_media_dir, quiz_name)
            os.makedirs(quiz_folder_in_media, exist_ok=True)

            file_path = os.path.join(quiz_folder_in_media, filename)
            with open(file_path, 'w') as f:
                json.dump(empty_data, f)

            images_folder_in_media = os.path.join(base_media_dir, 'Images')
            os.makedirs(images_folder_in_media, exist_ok=True)

            quiz = Quiz(
                name=quiz_name,
                json_test_data=os.path.join(base_media_dir, quiz_name, filename),
                count_questions=int(request.form['num-questions']),
                topic=request.form['topic'],
                description=request.form['description']
            )
            db.session.add(quiz)
            db.session.commit()

            session['quiz_name'] = quiz_name
            return redirect(url_for('New_Quiz.render_new_quiz', quiz_name=quiz_name))

        except Exception as e:
            print(f"Error while creating quiz: {e}")

    context = {
        'page': 'home',
        'is_auth': current_user.is_authenticated,
        'name': current_user.id
    }
    return render_template('New_Quiz_Settings.html', **context)


@login_required
def render_new_quiz_student():
    context = {
        'page': 'home',
        'is_auth': current_user.is_authenticated,
        'name': current_user.name
    }
    return render_template('New_Quiz_App_Student.html', **context)


@login_required
def render_new_quiz_2_student():
    context = {
        'page': 'home',
        'is_auth': current_user.is_authenticated,
        'name': current_user.name
    }
    return render_template('New_Quiz_App_Student_2.html', **context)


saved_topic = None

@login_required
def save_topic():
    data = request.get_json()
    topic = data.get('topic')

    if topic:
        if any(char in "абвгдеєжзиіїйклмнопрстуфхцчшщьюяАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ" for char in topic):
            language = "Ukrainian"
        elif any(char in string.ascii_letters for char in topic):
            language = "English"
        else:
            language = "Unknown"

        quiz_name = session.get('quiz_name')
        if quiz_name:
            base_media_dir = 'media'
            quiz_folder = os.path.join(base_media_dir, quiz_name)
            file_path = os.path.join(quiz_folder, 'json_data.json')

            quiz_data = []
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    quiz_data = json.load(f)

            quiz_data.append({
                'topic': topic,
                'language': language
            })

            with open(file_path, 'w') as f:
                json.dump(quiz_data, f, ensure_ascii=False, indent=4)

        return jsonify({"status": "success", "topic": topic, "language": language})
    else:
        return jsonify({"status": "error", "message": "No topic provided"}), 400