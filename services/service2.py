# instrumentação de serviços com o OpenTelemetry para enviar dados de rastreamento para o Jaeger
from flask import Flask
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
import time

app = Flask(__name__)

# Configurar o Tracer
resource = Resource(attributes={SERVICE_NAME: "service2"})
trace.set_tracer_provider(TracerProvider(resource=resource))
otlp_exporter = OTLPSpanExporter(endpoint="http://172.17.0.2:4317", insecure=True)
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(otlp_exporter))

# Instrumentar Flask
FlaskInstrumentor().instrument_app(app)

@app.route("/process")
def process():
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("service2-processing"):
        time.sleep(0.2)  # Simular processamento
        return "Processed by Service 2"

if __name__ == "__main__":
    app.run(port=5001)
