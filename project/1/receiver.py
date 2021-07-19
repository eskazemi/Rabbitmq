import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))  # todo connect to server rabbitmq

ch = connection.channel()

ch.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(f'Received {body}')


ch.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print('waiting message')

ch.start_consuming()
