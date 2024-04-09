#!/usr/bin/env python3
"""
A Basic Flask App
"""
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from typing import Dict, Optional
from datetime import datetime


class Config:
    """Babel Configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determines the best match with our supported languages"""
    locale = request.args.get("locale")
    if locale in Config.LANGUAGES:
        return locale
    if hasattr(g, 'user') and g.user and g.user["locale"] in Config.LANGUAGES:
        return g.user["locale"]
    return request.accept_languages.best_match(Config.LANGUAGES)


@babel.timezoneselector
def get_timezone() -> str:
    """Determines the timezone"""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if hasattr(g, 'user') and g.user and 'timezone' in g.user:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id: Optional[int] = None) -> Optional[Dict]:
    """Gets a user

    Keyword arguments:
    user_id -- The user's id
    Return: a user dictionary or None
    """
    login_as = request.args.get('login_as')
    if login_as:
        return users.get(int(login_as))
    return users.get(user_id)


@app.before_request
def before_request() -> None:
    """Runs before every request and adds a user attributes to flask.g"""
    g.user = get_user()


@app.route("/")
def index():
    """Renders the index page"""
    current_time = format_datetime(datetime.now())
    return render_template("7-index.html", current_time=current_time)


if __name__ == "__main__":
    app.run()
