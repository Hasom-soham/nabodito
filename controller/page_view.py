from flask import (Blueprint, render_template)

page_view = Blueprint("page_view_controller", __name__)


@page_view.route("/")
def home_page():
    return render_template("pages/home.html")
