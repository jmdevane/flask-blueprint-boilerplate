from flask import render_template, url_for, flash, redirect, Blueprint

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
@main.route("/index", methods=["GET", "POST"])
def index():

    return render_template("index.html", title="welcome")