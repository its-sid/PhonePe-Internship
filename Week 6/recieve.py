import pika, sys, os
credentials = pika.PlainCredentials('intern', 'intern')
def main():
  credentials = pika.PlainCredentials('intern', 'intern')
  connection = pika.BlockingConnection(pika.ConnectionParameters(host='intern2',virtual_host="host",credentials=credentials))
  channel = connection.channel()
  channel.queue_declare(queue='DATA',arguments = {"x-message-ttl" : 60000,"x-dead-letter-exchange" : '' ,"x-dead-letter-routing-key" : "DATA_SIDELINE" } )
  def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
  channel.basic_consume(queue='DATA', on_message_callback=callback, auto_ack=True)
  print(' [*] Waiting for messages. To exit press CTRL+C')
  channel.start_consuming()
if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print('Interrupted')
    try:
      sys.exit(0)
    except SystemExit:
      os._exit(0)