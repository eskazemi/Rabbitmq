import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))  # todo connect to server rabbitmq

ch1 = connection.channel()

ch1.queue_declare(queue='hello')

ch1.basic_publish(exchange='', routing_key='hello', body='salam')

print('message send')
connection.close()