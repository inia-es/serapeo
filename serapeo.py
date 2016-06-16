import plugins
import flask
import auth.controller

app = flask.Flask(__name__)

@app.route("/login", methods=['GET', 'POST'])
def on_login():
    return auth.controller.login(flask.request)

if __name__ == '__main__':
    app.run()
