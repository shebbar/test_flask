from flask import Flask, g
app = Flask(__name__)

from app.apis.blueprints import sample

app.register_blueprint(sample.bp)
