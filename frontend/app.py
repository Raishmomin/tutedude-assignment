from flask import Flask, jsonify, request, redirect, render_template
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)

BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:5000')


@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
        try:
            jsnForm = dict(request.form)
            print(f"Received name: {jsnForm}")
            requests.post(BACKEND_URL+'/submittodoitem', json=jsnForm)
            return redirect('/success')
        except Exception as e:
            error = str(e)
    
@app.route('/success')
def success():
    return 'Data submitted successfully'


if __name__ == '__main__':
    app.run(debug=True,port=3000)  
