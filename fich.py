#!/usr/bin/python
# -*- coding: Utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__,template_folder='./Template', static_folder='./Template')

@app.route("/")

def home():
    return render_template("./form.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9999)
