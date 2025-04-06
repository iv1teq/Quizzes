import flask

def show_page_registration():
    context = {'page': 'home'}
    return flask.render_template(template_name_or_list='registration.html', **context)