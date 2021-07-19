import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='topic_logs', exchange_type='topic')

message = {
    "error.warning.important": 'This is important message',
    "info.debug.notImportant": 'This is not important message',
}

for k, v in message.items():
    ch.basic_publish(exchange='topic_logs', routing_key=k, body=v)

print('send')
connection.close()
