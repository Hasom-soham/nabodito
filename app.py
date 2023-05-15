from flask import (Flask, redirect, url_for)
from controller.page_view import page_view

app = Flask(__name__)

app.register_blueprint(page_view)


@app.route("/")
def index():
    return redirect(url_for("page_view_controller.home_page"))


@app.route("/about")
def about():
    return redirect(url_for("page_view_controller.about_page"))
