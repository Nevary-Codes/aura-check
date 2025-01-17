from flask import Flask, request, jsonify, render_template, redirect, url_for
import os
import requests  # Import the requests library to make API calls

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

    
@app.route('/pred')
def preds():
    return render_template("pred.html")

if __name__ == '__main__':
    app.run(debug=True, port=6000)