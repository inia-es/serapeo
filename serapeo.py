import plugins
import flask

app = flask.Flask(__name__)

@app.route("/login")
def on_login():
    error = None
    url = ''
    if flask.request.method == 'GET':
        login_plugins = map ((lambda p: p.create_plugin().name), plugins.get_auth_plugins())
        return flask.render_template('login.html', login_plugins = login_plugins)

if __name__ == '__main__':
    app.run()
