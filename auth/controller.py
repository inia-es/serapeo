"""Controller for login

This controller solves authentification to the system, shows login page and
call the right auth plugin in order to grant accesss
"""
import plugins
import flask

def _get():
    login_plugins = plugins.get_auth_plugins()
    return flask.render_template('login.html', login_plugins=login_plugins)

def _post(request):
    plugin_name = request.form['auth_plugin']
    auth_plugin = plugins.get_auth_plugin(plugin_name)
    if auth_plugin is False:
        return _get()
    else:
        flat_form = dict(request.form.items())
        result = auth_plugin.validate(**flat_form)
        if result is False:
            return 'Login error'
        else:
            return 'User: ' + result

def login(request):
    """Solve GET or POST requests"""
    if request.method == 'GET':
        return _get()
    if request.method == 'POST':
        return _post(request)
