from flask import Flask

app = Flask(__name__)

app.debug = True

from views import select2, getData
