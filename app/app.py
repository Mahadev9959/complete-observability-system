
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import logging
import time

# OpenTelemetry imports
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# Configure OpenTelemetry
resource = Resource.create({
    "service.name": "observability-flask-app"
})

provider = TracerProvider(resource=resource)

otlp_exporter = OTLPSpanExporter(
    endpoint="http://jaeger:4318/v1/traces"
)

provider.add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

trace.set_tracer_provider(provider)

# Flask application
app = Flask(__name__)

# Enable automatic Flask tracing
FlaskInstrumentor().instrument_app(app)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)

metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    logger.info("Home page accessed")
    return jsonify({
        "message": "Welcome to Observability Project",
        "status": "running"
    })

@app.route("/health")
def health():
    logger.info("Health check requested")
    return jsonify({"status": "healthy"})

@app.route("/hello")
def hello():
    logger.info("Hello endpoint accessed")
    return jsonify({"message": "Hello from Flask Application"})

@app.route("/slow")
def slow():
    logger.info("Slow endpoint accessed")
    time.sleep(2)
    return jsonify({"message": "Slow response completed"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

