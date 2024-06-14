import pika

def send_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')

    channel.basic_publish(exchange='', routing_key='email_queue', body=message)
    print(f"Message sent: {message}")

    connection.close()

if __name__ == "__main__":
    message = "Hola, este es un mensaje de prueba por correo electrónico"
    send_message(message)
