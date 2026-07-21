from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

_leak_store = []

@app.route("/")
def home():
    return jsonify(status="ok", service="aiops-demo"), 200

@app.route("/crash")
def crash():
    data = None
    return jsonify(data["key"])  # this will raise an error on purpose

@app.route("/leak")
def leak():
    chunk = "x" * (10 * 1024 * 1024)  # 10MB string
    _leak_store.append(chunk)
    return jsonify(chunks_held=len(_leak_store)), 200
@app.route("/slow")
def slow():
    delay = random.uniform(2, 6)
    time.sleep(delay)
    return jsonify(delayed_seconds=delay), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)