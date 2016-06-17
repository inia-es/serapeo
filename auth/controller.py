import plugins
import flask

def _get(request):
    login_plugins = map ((lambda p: p.create_plugin()), plugins.get_auth_plugins())
    return flask.render_template('login.html', login_plugins = login_plugins)

def _post(request):
    plugin_name = request.form['auth_plugin']
    auth_plugin = plugins.get_auth_plugin(plugin_name)
    if auth_plugin == False:
        return _get(request)
    else:
        flat_form = dict(request.form.items())
        result = auth_plugin.create_plugin().validate(**flat_form)
        if result == False:
             return 'Login error'
        else:
             return 'User: ' + result

def login(request):
    if request.method == 'GET':
        return _get(request)
    if request.method == 'POST':
        return _post(request)
