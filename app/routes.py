from flask import Blueprint, render_template, request
from app.services import process_files

main_routes = Blueprint("main", __name__)

@main_routes.route("/", methods=["GET", "POST"])
def index():
    message = ""
    status = ""

    if request.method == "POST":
        path = request.form.get("path")
        mode = request.form.get("mode")

        success, result = process_files(path, mode)

        message = result
        status = "success" if success else "error"

    return render_template("index.html", message=message, status=status)

