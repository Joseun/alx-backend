#!/usr/bin/env python3
"""
Creating an i18n application
"""

from flask import Flask, render_template
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config():
    """ Configuration class for Babel """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')


@babel.localselector
def get_locale() -> str:
    """ determine the best match with supported languages based on locale """
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> str:
    """ Home page """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
