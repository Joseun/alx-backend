#!/usr/bin/env python3
"""
Creating an i18n application
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from typing import Union, Dict
from pytz import timezone
import pytz


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """ Configuration class for Babel """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')


def get_user() -> Union[Dict, None]:
    """Get a user information"""
    id = request.args.get('login_as')
    if id:
        try:
            id = int(id)
        except ValueError:
            id = None
    if id:
        return users.get(id)
    return None


@app.before_request
def before_request() -> None:
    """ Get users details before request"""
    g.user = get_user()


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> str:
    """ Home page """
    return render_template('4-index.html')


@babel.localselector
def get_locale() -> str:
    """ determine the best match with supported languages based on locale """
    locale = request.args.get('locale')
    if not locale and g.user:
        locale = g.user.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone(my_timezone=None) -> str:
    """Function to get time zone of user"""
    my_timezone = request.args.get('timezone')
    if not my_timezone and g.user:
        my_timezone = g.user.get('timezone')
    if my_timezone:
        try:
            tz = timezone(my_timezone)
            return tz
        except pytz.exceptions.UnknownTimeZoneError:
            return timezone(Config.BABEL_DEFAULT_TIMEZONE)
    else:
        return timezone(Config.BABEL_DEFAULT_TIMEZONE)

if __name__ == "__main__":
    app.run()
