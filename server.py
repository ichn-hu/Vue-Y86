from flask import Flask, request
from flask import jsonify
import pprint
app = Flask(__name__)

@app.route('/')
def show():
    return open('./frontend/experiment/get-data/index.html', 'r').read()

@app.route("/upload", methods=['POST', 'GET'])
def run():
    instrCode = request.__dict__
    pp = pprint.PrettyPrinter()
    pp.pprint(instrCode)
    return 'ok'

if __name__ == "__main__":
    app.run(port=8080)
