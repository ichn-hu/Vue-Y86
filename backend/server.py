from flask import Flask, request
from flask_cors import CORS
import json
import pprint
from kernel import runner
app = Flask(__name__, static_folder='../static')
cors = CORS(app, resourses={r"/*": {"origins": "*"}})

@app.route('/')
def show():
    return open('./index.html', 'r').read()

@app.route("/upload", methods=['POST', 'GET'])
def run():
    instrCode = request.form.get('instrCode')
    result = runner.runInstrCode(instrCode)
    dump = json.dumps(result)
    print(len(dump))
    return dump

if __name__ == "__main__":
    app.run(port=5000)
