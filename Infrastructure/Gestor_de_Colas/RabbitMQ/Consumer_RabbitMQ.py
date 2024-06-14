import pika
import smtplib
from email.mime.text import MIMEText

def send_email(body):
    sender_email = "oscar.albornoz@udla.edu.ec"
    receiver_email = "oscaremilioalbornoz@hotmail.com"
    password = "Emilianooo"

    msg = MIMEText(body)
    msg['Subject'] = 'Test Email'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP('mail.smtp2go.com', 2525) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"Email sent to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def callback(ch, method, properties, body):
    message = body.decode()
    print(f"Received message: {message}")
    send_email(message)

def consume_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')

    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)
    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    consume_message()
