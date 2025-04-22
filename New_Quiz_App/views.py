from flask import request, render_template
from .models import Quiz
from project.settings import db
import flask

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
            quiz = Quiz(
                name=request.form['name'],
                json_test_data=request.form['json_test_data'], 
                count_questions=int(request.form['count_questions']),
                topic=request.form['topic'],
                image=request.form['image'],  
                description=request.form['description']
            )
            db.session.add(quiz)
            db.session.commit()
        except Exception as e:
            print(e)

    context = {'page': 'home'}
    return render_template('New_Quiz_Settings.html', **context)