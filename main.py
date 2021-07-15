from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Welcome!</h1>'
