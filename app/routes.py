from flask import Blueprint, render_template

bp = Blueprint("main", __name__)

@bp.route("/")
def home():
    return render_template("index.html", title="Home")

@bp.route("/about")
def about():
    return render_template("about.html", title="About")
