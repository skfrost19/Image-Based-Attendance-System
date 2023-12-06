# create a flask app
import time
import os
import flask
from flask import request, render_template
from flask import send_file
from werkzeug.utils import secure_filename
from datetime import datetime
from src.components.pipeline import pipeline

# create  a flask app
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# Route for getting image from user
@app.route("/upload-image", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return "No file part", 400
    file = request.files["file"]

    filename = secure_filename(file.filename).split(".")
    new_filename = datetime.now().strftime("%d-%m-%Y") + "." + filename[-1]
    file.filename = new_filename
    file_path = os.path.join(os.getcwd(), "images", file.filename)
    file.save(file_path)
    pipeline(file_path)

    return "Image uploaded and processed", 200


# Route for giving back CSV
@app.route("/download-csv", methods=["GET"])
def download_csv():
    return send_file(
        os.path.join(os.getcwd(), "attendance", "attendance.csv"), as_attachment=True
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)
