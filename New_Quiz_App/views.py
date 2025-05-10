from flask import request, render_template, redirect, url_for
from .models import Quiz
from project.settings import db
from flask_login import login_required, current_user
import os
import json

# Для учителей

@login_required
def render_new_quiz():
    # if not current_user.is_admin:
    #     return render_template('error_403.html')

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
            filename = f"{quiz_name}.json"
            empty_data = []

            file_path = os.path.join('New_Quiz_App', 'static', 'quiz_data', filename)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            with open(file_path, 'w') as f:
                json.dump(empty_data, f)

            quiz = Quiz(
                name=quiz_name,
                json_test_data=filename,
                count_questions=int(request.form['num-questions']),
                topic=request.form['topic'],
                description=request.form['description']
            )
            db.session.add(quiz)
            db.session.commit()

            return redirect(url_for('New_Quiz.render_new_quiz'))

        except Exception as e:
            print(e)

    context = {
        'page': 'home',
        'is_auth': current_user.is_authenticated,
        'name': current_user.id
    }
    return render_template('New_Quiz_Settings.html', **context)


# Для студентов

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
