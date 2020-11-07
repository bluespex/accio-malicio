from flask import Flask, render_template, request, abort
from flask_cors import CORS
import json
import os
import subprocess
import sys

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    with open(os.path.join(os.getcwd() , 'details.json')) as f:
        data = json.load(f)
    return data

@app.route('/report')
def report():
    with open(os.path.join(os.getcwd() , 'db.json')) as f:
        data = json.load(f)
    return data

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        credentials = request.json

        subprocess.Popen("app.py " + credentials['email'] + " " + credentials['password'], shell=True)
        # print("app.py " + credentials['email'] + " " + credentials['password'], file= sys.stderr)
        return credentials


if __name__ == '__main__':
    app.run(debug=True)