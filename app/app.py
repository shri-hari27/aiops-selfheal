from flask import Flask, jsonify
import os
import time
import random

app = Flask(__name__)

memory_chunks = []
ready = True

APP_NAME = os.getenv("APP_NAME", "AIOps Self-Healing Demo")
ENVIRONMENT = os.getenv("ENVIRONMENT", "Production")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
VERSION = os.getenv("VERSION", "v2.0")
API_KEY = os.getenv("API_KEY")


@app.route("/")
def home():
    return jsonify({
        "service": APP_NAME,
        "status": "ok",
        "environment": ENVIRONMENT,
        "version": VERSION,
        "log_level": LOG_LEVEL
    })


@app.route("/config")
def config():
    return jsonify({
        "app": APP_NAME,
        "environment": ENVIRONMENT,
        "log_level": LOG_LEVEL,
        "api_key_loaded": API_KEY is not None,
        "version": VERSION
    })


@app.route("/health/live")
def live():
    return jsonify({
        "status": "alive",
        "version": VERSION
    })


@app.route("/health/ready")
def readiness():
    global ready

    if ready:
        return jsonify({
            "status": "ready",
            "version": VERSION
        }), 200

    return jsonify({
        "status": "not ready"
    }), 503


@app.route("/ready/off")
def ready_off():
    global ready
    ready = False
    return jsonify({"readiness": "disabled"})


@app.route("/ready/on")
def ready_on():
    global ready
    ready = True
    return jsonify({"readiness": "enabled"})


@app.route("/slow")
def slow():
    delay = random.randint(2, 6)
    time.sleep(delay)

    return jsonify({
        "delay": delay,
        "version": VERSION
    })


@app.route("/leak")
def leak():
    memory_chunks.append(bytearray(10 * 1024 * 1024))

    return jsonify({
        "chunks": len(memory_chunks),
        "memory_allocated_mb": len(memory_chunks) * 10,
        "version": VERSION
    })


@app.route("/crash")
def crash():
    os._exit(1)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)