from app import app
from flask import render_template


@app.route("/")
def index():
    return "Sever is Active"


@app.route("/test")
def get_context():
    options = []
    for i in range(0, 20000):
        temp = str(i + 1)
        while len(temp) < 5:
            temp = '0' + temp
        options.append(temp)

    data = {
        'options': options
    }
    return render_template('select2.html', title='Home', data=data)
