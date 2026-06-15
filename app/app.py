from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter, Gauge
import random
import time

app = Flask(__name__)

metrics = PrometheusMetrics(app)

REQUESTS = Counter(
    "app_requests_total",
    "Total API requests"
)

ACTIVE_USERS = Gauge(
    "app_active_users",
    "Current active users"
)

@app.route("/")
def home():
    REQUESTS.inc()
    ACTIVE_USERS.set(random.randint(10, 100))

    return jsonify({
        "project": "CloudOps Observability Platform",
        "status": "running"
    })

@app.route("/api/orders")
def orders():
    REQUESTS.inc()

    return jsonify({
        "orders": random.randint(100, 1000),
        "timestamp": time.time()
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
