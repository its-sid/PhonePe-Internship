import psutil
import time
import requests
import json
from riemann_client.transport import TCPTransport
from riemann_client.client import QueuedClient
while True:
    with QueuedClient(TCPTransport("192.168.3.7", 5555)) as client:


        data = requests.get(url = "http://192.168.0.126:15672/api/overview" ,auth=('sid','sid'),headers={'content-type': 'application/json'})

        json_data = json.loads(data.text)
        #Cpu percentage
        client.event(service="cpu_per", metric_f=psutil.cpu_percent(interval=None, percpu=False))

        client.event(service="memory_per", metric_f=psutil.virtual_memory().percent)
        
        client.event(service="disk_per", metric_f=psutil.disk_usage('/').percent)

        client.event(service="memory_free", metric_f=psutil.virtual_memory().free)

        client.event(service="rmq_msgs", metric_f=json_data["queue_totals"]["messages"])

        client.flush()

    time.sleep(10)