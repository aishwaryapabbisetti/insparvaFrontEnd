from app import app
from flask import render_template


@app.route("/")
def index():
    return "Sever is Active"


@app.route("/test")
def get_context():
    context = { 'message': 'Hope it works' }
    return render_template('baseTemplate.html', title='Home', context=context)
