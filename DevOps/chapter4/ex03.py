#!/usr/bin/python3
from flask import Flask, redirect, request

app = Flask('basic app')

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect("http://google.com")
    else:
        return "<h1>GET request from Flask</h1>"