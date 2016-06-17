"""Serapeo app

Serapeo is a Flask-based ETL tool for sync metadata in differents repositories
"""

import flask
import auth.controller

APP = flask.Flask(__name__)

@APP.route("/login", methods=['GET', 'POST'])
def on_login():
    """Call login controller"""
    return auth.controller.login(flask.request)

if __name__ == '__main__':
    APP.run()
