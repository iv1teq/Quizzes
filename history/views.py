from flask_login import current_user
import flask

def show_history_page():
    
    return flask.render_template(template_name_or_list="history.html" )
    context = {'page': 'history'}

def show_qsr_page():
    
    return flask.render_template(template_name_or_list="quiz_student_result.html" )
    context = {'page': 'history',
               'name': current_user.name,
                'email': current_user.email,
                }

def show_qtr_page():
    
    return flask.render_template(template_name_or_list="quiz_teacher_result.html" )
    context = {'page': 'history'}
   