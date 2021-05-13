from flask import Flask, jsonify, Response, abort,request
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/', methods=['POST'])
def callback():
    print("received hook")
    json_data = request.json()
    print(json_data, indent=4)
    return Response(status=200)


if __name__ == "__main__":
    app.run()
    # app.run(host='127.0.0.1', port=80, debug=True)