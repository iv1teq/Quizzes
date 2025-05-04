from flask import request, render_template, redirect, url_for, jsonify
from .models import Quiz
from project.settings import db
import flask
import os
import json
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

@login_required
def render_new_quiz():
    context = {
        'page': 'home',
        'is_auth': current_user.is_authenticated,
        'name': current_user.name
    }
    return flask.render_template('New_Quiz_App.html', **context)

@login_required
def render_new_quiz_2():
    context = {
        'page': 'home',
        'is_auth': current_user.is_authenticated,
        'name': current_user.name
    }
    return flask.render_template('New_Quiz_App_2.html', **context)

@login_required
def render_new_quiz_student():
    context = {
        'page': 'home',
        'is_auth': current_user.is_authenticated,
        'name': current_user.name
    }
    return flask.render_template('New_Quiz_App_Student.html', **context)

@login_required
def render_new_quiz_2_student():
    context = {
        'page': 'home',
        'is_auth': current_user.is_authenticated,
        'name': current_user.name
    }
    return flask.render_template('New_Quiz_App_Student_2.html', **context)






DIR = os.path.dirname(os.path.abspath(__file__))


@login_required
def render_new_quiz_settigs():
    if request.method == 'POST':
        try:
            quiz_name = request.form['quiz-name'] 
            filename = f"{quiz_name}.json"
            empty_data = []

            
            file_path = os.path.join(DIR, 'static', 'quiz_data', filename)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                json.dump(empty_data, f)

            
            image = request.files.get('image')
            image_filename = None
            if image and image.filename != '':
                image_filename = secure_filename(image.filename)
                media_folder = os.path.join(DIR, 'static', 'media')
                os.makedirs(media_folder, exist_ok=True)
                image_path = os.path.join(media_folder, image_filename)
                image.save(image_path)

            
            quiz = Quiz(
                name=quiz_name,
                json_test_data=filename,
                count_questions=int(request.form['num-questions']),
                topic=request.form['topic'],
                image=f"new_quiz/media/{image_filename}" if image_filename else None,
                description=request.form['description']
            )

            db.session.add(quiz)
            db.session.commit()

            return redirect(url_for('New_Quiz.render_new_quiz'))

        except Exception as e:
            print(f"Ошибка: {e}")

    context = {
        'page': 'home',
        'is_auth': current_user.is_authenticated,
        'name': current_user.name
    }
    return render_template('New_Quiz_Settings.html', **context)
