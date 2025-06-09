from flask import Flask, jsonify, request, redirect, render_template
from pymongo import MongoClient
import json
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)


@app.route('/api')
def get_data():
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)


MONGO_URI = os.getenv('MONGO_URI')

# MongoDB Atlas setup
client = MongoClient(MONGO_URI)  
db = client['test']
collection = db['flask-tutorial']


@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    print("Received request to submit todo item",request)
    frmData = dict(request.json)
    collection.insert_one(frmData)

    return redirect('/success')  

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Ensure the port is set to 5000
