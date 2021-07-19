import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()

ch.exchange_declare(exchange='direct_log', exchange_type='direct')

result = ch.queue_declare(queue='', exclusive=True)
queue = result.method.queue
logs = ('info', 'warning', 'error')

for log in logs:
    ch.queue_bind(exchange='direct_log', queue=queue, routing_key=log)

print('Waiting for message')


def callback(ch, method, properties, body):
    print(f'Received {body} {method.routing_key}')


ch.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
ch.start_consuming()
