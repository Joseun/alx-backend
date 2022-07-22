#!/usr/bin/env python3
"""
Creating an i18n application
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config():
    """ Configuration class for Babel """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> str:
    """ Home page """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
