#!/usr/bin/env python3
"""
A Basic Flask App
"""
from flask import Flask, render_template, request
from flask_babel import Babel


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
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def index():
    """Renders the index page"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
