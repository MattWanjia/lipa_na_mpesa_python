from flask import Flask, request, jsonify, Response, abort
from flask_ngrok import run_with_ngrok
import requests
from flask_mpesa import MpesaAPI
import time
import json
from requests.auth import HTTPBasicAuth
import base64

app = Flask(__name__)
run_with_ngrok(app)

@app.route("/callback", methods=['POST'])
def callback():
    # get json data set to this route
    if request.method == "POST":
        print("received hook")
        json_data_bytes = request.data
        json_data = json_data_bytes.decode('utf-8')
        print(json_data)
        return Response(status=200)


if __name__ == "__main__":
    # app.run('127.0.0.1', port=80, debug=True)
    app.run()