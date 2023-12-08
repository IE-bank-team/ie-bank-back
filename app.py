from iebank_api import app
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter
import os

# Set up Azure Monitor Trace Exporter
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

exporter = AzureMonitorTraceExporter(
    connection_string=f"InstrumentationKey={os.getenv('APPINSIGHTS_INSTRUMENTATIONKEY')}"
)

span_processor = BatchSpanProcessor(exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

if __name__ == '__main__':
    app.run(debug=True)
