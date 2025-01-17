from flask import Flask, request, jsonify, render_template, redirect, url_for
import os
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index-main.html')

    
@app.route('/pred')
def preds():
    return render_template("index.html")

@app.route('/quiz')
def quiz():
    return render_template("quiz.html")

@app.route('/tech')
def tech():
    return render_template("tech.html")

if __name__ == '__main__':
    app.run(debug=True, port=6000)