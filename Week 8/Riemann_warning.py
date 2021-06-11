import psutil
import time
from riemann_client.transport import TCPTransport
from riemann_client.client import QueuedClient
while True:
    with QueuedClient(TCPTransport("192.168.3.7", 5555)) as client:
        f = psutil.virtual_memory().percent
        if f > 70: state="warning"
        if f > 80: state="critical"
        client.event(service="memory_per", metric_f= f ,state = state)
        d = psutil.disk_usage('/').percent
        if d > 70: state="warning"
        if d > 80: state="critical"
        client.event(service="disk_per", metric_f= d, ,state = state)
        client.flush()
    time.sleep(10)