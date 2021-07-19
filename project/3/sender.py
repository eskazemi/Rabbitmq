import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))  # todo connect to server rabbitmq

ch1 = connection.channel()

ch1.exchange_declare(exchange='logs', exchange_type='fanout')

ch1.basic_publish(exchange='logs', routing_key='', body="salam")
print('message send')
connection.close()

