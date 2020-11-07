from flask import Flask

import json
import os


app = Flask(__name__)

@app.route('/')
def home():
    with open(os.path.join(os.getcwd() , 'hashdb.json')) as f:
        data = json.load(f)
    return data
    

if __name__ == '__main__':
    app.run(debug=True)