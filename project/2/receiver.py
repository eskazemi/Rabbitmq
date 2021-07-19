import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))  # todo connect to server rabbitmq

ch2 = connection.channel()

ch2.queue_declare(queue='first')


def callback(ch, method, properties, body):
    print(f'Received {body}')
    time.sleep(9)
    print(properties.headers)
    print('Done')
    ch.basic_ack(delivery_tag=method.delivery_tag)


ch2.basic_qos(prefetch_count=1)
ch2.basic_consume(queue='hello', on_message_callback=callback, )

print('waiting message')

ch2.start_consuming()
