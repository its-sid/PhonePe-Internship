import pika
import time
t=0
credentials = pika.PlainCredentials('intern', 'intern')
connection = pika.BlockingConnection(
  pika.ConnectionParameters(host='intern1',virtual_host="host",credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='DATA_SIDELINE')
channel.queue_declare(queue='DATA',arguments = {"x-message-ttl" : 60000,"x-dead-letter-exchange" : '' ,"x-dead-letter-routing-key" : "DATA_SIDELINE" } )
while 1:
    channel.basic_publish(exchange='', routing_key='DATA', body="MessageNo :- {}".format(t) )
    print(" Msg Send : MessageNo :- {}".format(t))
    t=t+1
    time.sleep(1)
connection.close()