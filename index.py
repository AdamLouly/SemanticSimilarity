from flask import Flask, request, jsonify
import requests, json
import os
import random
from flask_cors import CORS, cross_origin
from app.bert import *

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def index():
    return "Hello 1"

@app.route('/api/calculateSimilarity/', methods=['POST'])
def calculateSimilarity():
    if request.method == 'POST':
        data = request.json
        question = data["question"]
        others = data["questions"]
        i=0
        for item in data["questions"]:
            data["questions"][i].update({"score":NextSentenceScore(question,item["question"])})
            i=i+1
        data["questions"]=sorted(data["questions"], key = lambda i: i['score'],reverse=True) 
    return jsonify(data), 201


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port = 5055,debug=True)
