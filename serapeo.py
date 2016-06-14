from werkzeug.wsgi import SharedDataMiddleware
import os
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException
from jinja2 import Environment, FileSystemLoader

class Serapeo(object):

    def __init__(self):
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)
        self.url_map = Map([
            Rule('/login', endpoint='login'),
        ])

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, 'on_' + endpoint)(request, **values)
        except HTTPException, e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def on_login(self, request):
        error = None
        url = ''
        if request.method == 'GET':
            print(plugins.get_auth_plugins())
            return self.render_template('login.html')


def create_app(with_static=True):
    app = Serapeo()
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/assets': os.path.join(os.path.dirname(__file__), 'assets')
        })
    return app


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=False, use_reloader=True)
