import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))  # todo connect to server rabbitmq

ch1 = connection.channel()

ch1.queue_declare(queue='first', durable=True)

message = 'the test message'
ch1.basic_publish(exchange='', routing_key='first', body=message, properties=pika.BasicProperties(delivery_mode=2, headers={'name': 'ali'}))
print('message send')
connection.close()

