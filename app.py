from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 8080))

# Prometheus metric
hello_world_counter = Counter(
    "root_access_total",
    "Total number of accesses to the root path"
)

@app.route("/my-app")
def my_app():
    hello_world_counter.inc()
    return "Hello, World! 206"

@app.route("/about")
def about():
    return "This is a sample Python application for Kubernetes deployment testing."

@app.route("/ready")
def ready():
    return "Ready", 200

@app.route("/live")
def live():
    return "Alive", 200

@app.route("/classified")
def classified():
    return "You should not be here!!!", 200

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
