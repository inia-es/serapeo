import plugins
import flask

app = flask.Flask(__name__)

@app.route("/login", methods=['GET', 'POST'])
def on_login():
    error = None
    url = ''
    if flask.request.method == 'GET':
        return get_login()
    if flask.request.method == 'POST':
        plugin_name = flask.request.form['auth_plugin']
        auth_plugin = plugins.get_auth_plugin(plugin_name)
        if auth_plugin == False:
            return get_login()
        else:
            result = auth_plugin.create_plugin().validate(flask.request.form)
            if result == False:
                 return 'Login error'
            else:
                 return 'User: ' + result
            

def get_login():
        login_plugins = map ((lambda p: p.create_plugin()), plugins.get_auth_plugins())
        return flask.render_template('login.html', login_plugins = login_plugins)


if __name__ == '__main__':
    app.run()
