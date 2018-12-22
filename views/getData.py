from app import app
from flask import request


@app.route('/get_data', methods=['POST'])
def get_data():
    return "Hello " + request.form['testName']
