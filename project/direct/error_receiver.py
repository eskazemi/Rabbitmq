import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()

ch.exchange_declare(exchange='direct_log', exchange_type='direct')
result = ch.queue_declare(queue='', exclusive=True)
qname = result.method.queue
log = 'error'
ch.queue_bind(exchange='direct_log', queue=qname, routing_key=log)

print('Waiting for message')


def callback(ch, method, properties, body):
    with open('error_logs.log', 'a') as lg:
        lg.write(f'{str(body)}' + '\n')


ch.basic_consume(queue=qname, on_message_callback=callback, auto_ack=True)
ch.start_consuming()
