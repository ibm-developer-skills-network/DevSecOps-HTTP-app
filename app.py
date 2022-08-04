import os
import requests
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from flask_talisman import Talisman

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

csp = {
    'default-src': '\'self\''
}
# talisman = Talisman(app, content_security_policy=csp)
# CORS(app, resources={"/*": {"origins": "http://localhost:3000"}})

@app.route('/')
@app.route('/hello')
def hello():
    response = '<h1>Hello, human!</h1>'
    return response

# 404
@app.route('/404')
def not_found():
    abort(404)

@app.route('/serve')
def serve_data():
    raw = requests.get('https://jsonplaceholder.typicode.com/posts/1/comments')
    data = raw.json()
    return jsonify(data)
