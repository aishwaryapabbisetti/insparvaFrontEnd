from app import app
from flask import render_template


@app.route("/")
def index():
    return "Sever is Active"


@app.route("/select")
def get_context():
    selected_options = []
    options = []
    for i in range(0, 20000):
        temp = str(i + 1)
        while len(temp) < 5:
            temp = '0' + temp
        options.append(temp)
        if i % 5 == 0 and len(selected_options) <= 5:
            selected_options.append(temp)
    data = {
        'options': options,
        'selected_options': selected_options
    }
    return render_template('select2.html', title='Home', data=data)
