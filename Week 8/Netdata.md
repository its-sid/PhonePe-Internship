## Install Netdata :-

To install netdata we have used bash script provided by the official Website
```bash
bash <(curl -Ss https://my-netdata.io/kickstart.sh)
```
Referred links:-

https://learn.netdata.cloud/docs/get-started

By default Netdata auto-detects thousands of data sources and immediately collects per-second metrics.

## Configure netdata to collect and display RabbitMQ data

To collect data netdata uses rabbitmq management plugin, so rabbitmq management plugin should be turned on
Netdata provide a python plugin to capture data from management plugin.

To Configure plugin we will add the following in conf dir (/etc/netdata)
Add a rmq config file using:-
```bash    
sudo ./edit-config python.d/rabbitmq.conf
```

Add Username, Password and IP address of RMQ server to connect such as:-

    local:
        host: '127.0.0.1'
        user: 'sid'
        pass: 'sid'

Referred links :-

https://learn.netdata.cloud/docs/agent/collectors/python.d.plugin/rabbitmq

>Other alternatives of Netdata are collectd and telegraf

## Some advantages of Netdata:

1. It can replace collectd + riemann + grafana
2. Collects most available metrics automatically from system (no configuration needed)
3. Plugin suppport for most of the data stores
4. Sofisticated alarming
5. Support time series backends
6. Lightweight ,small memory footprint

## Some disadvantages of Netdata:-

1. Collectd is written in C and lightweight then netdata


Some Referred links :

https://techietown.info/2017/05/comparing-collectdtelegraf-netdata/


