from flask import (Flask, redirect, url_for)
from controller.page_view import page_view

app = Flask(__name__)

app.register_blueprint(page_view)


@app.route("/")
def index():
    return redirect(url_for("page_view_controller.home_page"))


if __name__ == '__main__':
    app.run()
