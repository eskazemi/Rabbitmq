import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()

ch.exchange_declare(exchange='direct_log', exchange_type='direct')

message = {
    "info": "This is info message",
    "error": "This is error message",
    "warning": "This is warning message"
}
for k, v in message.items():
    ch.basic_publish(exchange='direct_log', routing_key=k, body=v)
print('message send')
connection.close()
