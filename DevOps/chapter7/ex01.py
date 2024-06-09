import prometheus_client
import time
from time import sleep
import random

from flask import Response, Flask
from prometheus_client import Counter, Histogram

app = Flask("prometheus-app")

REQUESTS =  Counter(
    'requests', 'Application request count',
    ['endpoint']
)

TIMER = Histogram(
    'slow', 'Slow Requests',
    ['endpoint']
)

@app.route("/")
def index():
    # счетчик запросов к /
    REQUESTS.labels(endpoint='/').inc()
    return "<h1>Developer Prometheus-back Flask App</h1>"

@app.route("/metrics")
def metrics():
    return Response(
        prometheus_client.generate_latest(),
        mimetype="text/plain; version=0.0.4; charset=utf-8"
    )

@app.route("/database") 
def database():
    with TIMER.labels('/database').time():
        # время отклика БД
        sleep(random.uniform(1, 3))
    return "<h1>Complete expensive database operation</h1>"
