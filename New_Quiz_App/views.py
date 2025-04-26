from flask import request, render_template
from .models import Quiz
from project.settings import db
import flask
import os
import json
from flask import redirect, url_for
from flask import jsonify

def render_new_quiz():
    context = {'page': 'home'}
    return flask.render_template('New_Quiz_App.html', **context)

def render_new_quiz_2():
    context = {'page': 'home'}
    return flask.render_template('New_Quiz_App_2.html', **context)


def render_new_quiz_student():
    context = {'page': 'home'}
    return flask.render_template('New_Quiz_App_Student.html', **context)

def render_new_quiz_2_student():
    context = {'page': 'home'}
    return flask.render_template('New_Quiz_App_Student_2.html', **context)

def render_new_quiz_settigs():
    if request.method == 'POST':
        try:
            quiz_name = request.form['name']
            filename = f"{quiz_name}.json"


            empty_data = []
            file_path = os.path.join('New_Quiz_App', 'static', 'quiz_data', filename)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                json.dump(empty_data, f)


            quiz = Quiz(
                name=quiz_name,
                json_test_data=filename,  
                count_questions=int(request.form['count_questions']),
                topic=request.form['topic'],
                image=request.form['image'],
                description=request.form['description']
            )
            db.session.add(quiz)
            db.session.commit()

    
            return redirect(url_for('New_Quiz.render_new_quiz'))

        except Exception as e:
            print(e)

    context = {'page': 'home'}
    return render_template('New_Quiz_Settings.html', **context)

