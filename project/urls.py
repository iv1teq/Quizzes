import home_app,registration

from .settings import project


home_app.home.add_url_rule(rule= '/', view_func=home_app.show_home_page, methods = ['POST', 'GET'])

registration.registration.add_url_rule(rule = '/registration', view_func= registration.show_page_registration, methods = ['POST', 'GET'])
project.register_blueprint(registration.registration)
project.register_blueprint(blueprint=home_app.home)