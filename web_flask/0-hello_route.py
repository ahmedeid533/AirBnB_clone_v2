#!/usr/bin/python3
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'