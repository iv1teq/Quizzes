import home_app, New_Quiz_App, registration, authorization 

from profile.app import profille
from profile.views import show_profile_page

from .settings import project


home_app.home.add_url_rule(rule= '/', view_func=home_app.show_home_page, methods = ['POST', 'GET'])
registration.registration.add_url_rule(rule = '/registration', view_func= registration.show_page_registration, methods = ['POST', 'GET'])
New_Quiz_App.New_Quiz.add_url_rule(rule='/new-quiz', view_func=New_Quiz_App.render_new_quiz_settings, methods = ['POST','GET'])
New_Quiz_App.New_Quiz.add_url_rule(rule= '/new-quiz-2', view_func=New_Quiz_App.render_new_quiz, methods = ['POST', 'GET'])
New_Quiz_App.New_Quiz.add_url_rule(rule= '/new-quiz-3', view_func=New_Quiz_App.render_new_quiz_2, methods = ['POST', 'GET'])
authorization.authorization.add_url_rule( rule = "/login", view_func = authorization.show_authorization, methods = ['POST', 'GET'])
profille.add_url_rule(rule= '/profile', view_func=show_profile_page, methods = ['POST', 'GET'])


project.register_blueprint(blueprint=home_app.home)
project.register_blueprint(registration.registration)
project.register_blueprint(authorization.authorization)
project.register_blueprint(blueprint=New_Quiz_App.New_Quiz)
project.register_blueprint(blueprint=profille)











