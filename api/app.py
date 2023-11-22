# create a flask app
import flask
from flask import request, jsonify, render_template
from flask import send_file
from werkzeug.utils import secure_filename
import json
import os
import sys
from datetime import datetime

# create  a flask app
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
        return render_template('index.html')

# Route for getting image from user
@app.route('/upload-image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    filename = secure_filename(file.filename).split('.')
    new_filename = datetime.now().strftime("%d-%m-%Y") + '.' + filename[-1] 
    # change filename to 
    print(os.path.join('images', new_filename))
    file.save(os.path.join('images', new_filename))  # assuming you have a directory named 'uploads'
    
    # run main.py in the parent directory
    os.system('python main.py')
    return 'Image uploaded and processed', 200

# Route for giving back CSV
@app.route('/download-csv', methods=['GET'])
def download_csv():
    # Assuming you have a CSV file named 'output.csv' in a directory named 'outputs'
    return send_file(os.path.join('..\\attendance\\attendance.csv'), as_attachment=True)

if __name__ == "__main__":
    app.run(port=5000, debug=True)