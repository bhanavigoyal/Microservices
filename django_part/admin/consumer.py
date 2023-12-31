import pika, json, os, django

os.environ.setdefault('DJANGO_SETTTINGS_MODULE', 'admin.settings')
django.setup()

from products import Product
params = pika.URLParameters('amqps://twzmwzsm:41M5cczpbhpJ1pjkGVkHkaJssUvuci4O@puffin.rmq2.cloudamqp.com/twzmwzsm')
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Recieved in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes+1
    product.save()
    print('Product likes increased')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()