from flask import Flask, jsonify
import random
import time
import os

app = Flask(__name__)

_leak_store = []

APP_NAME = os.getenv("APP_NAME", "AIOps Demo")
ENVIRONMENT = os.getenv("ENVIRONMENT", "Development")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
API_KEY = os.getenv("API_KEY", "NOT_SET")


@app.route("/")
def home():
    return jsonify(
        status="ok",
        service=APP_NAME,
        environment=ENVIRONMENT,
        log_level=LOG_LEVEL
    ), 200


@app.route("/health/live")
def live():
    return jsonify(status="alive"), 200


@app.route("/health/ready")
def ready():
    return jsonify(status="ready"), 200


@app.route("/config")
def config():
    return jsonify(
        app=APP_NAME,
        environment=ENVIRONMENT,
        log_level=LOG_LEVEL,
        api_key_loaded=(API_KEY != "NOT_SET")
    )


@app.route("/crash")
def crash():
    raise RuntimeError("Intentional crash for Kubernetes demo")


@app.route("/leak")
def leak():
    chunk = "x" * (10 * 1024 * 1024)
    _leak_store.append(chunk)

    return jsonify(
        chunks=len(_leak_store),
        memory_allocated_mb=len(_leak_store) * 10
    )


@app.route("/slow")
def slow():

    delay = random.uniform(2,6)

    time.sleep(delay)

    return jsonify(delay=delay)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)