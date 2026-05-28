# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:36:17 2026

@author: huawei
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)