import pika, json

params = pika.URLParameters('amqps://twzmwzsm:41M5cczpbhpJ1pjkGVkHkaJssUvuci4O@puffin.rmq2.cloudamqp.com/twzmwzsm')
connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties= pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
    #hello