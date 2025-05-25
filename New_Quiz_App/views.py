from flask import request, render_template, redirect, url_for
from .models import Quiz
from project.settings import db
from flask_login import login_required, current_user
import os
import json

@login_required
def render_new_quiz():
    if not current_user.is_admin:
        return render_template('error_403.html')

    context = {
        'page': 'home',
        'is_auth': current_user.is_authenticated,
        'name': current_user.name
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

            return redirect(url_for('New_Quiz.render_new_quiz'))

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