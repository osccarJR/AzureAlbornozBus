import json
from azure.servicebus import ServiceBusMessage
from Infrastructure.Gestor_de_Colas.Azure.Connection_Azure import get_servicebus_client, QUEUE_NAME
from EventProducer.Domain.Alert_Event import AlertEvent
import smtplib
from email.mime.text import MIMEText

def send_message(alert_event):
    servicebus_client = get_servicebus_client()
    with servicebus_client:
        sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
        with sender:
            message_dict = alert_event.to_dict()
            servicebus_message = ServiceBusMessage(json.dumps(message_dict))
            sender.send_messages(servicebus_message)
            print(f"Message sent: {servicebus_message}")

def consume_message():
    servicebus_client = get_servicebus_client()
    with servicebus_client:
        receiver = servicebus_client.get_queue_receiver(queue_name=QUEUE_NAME, max_wait_time=5)
        with receiver:
            for msg in receiver:
                message_data = json.loads(str(msg))
                alert_event = AlertEvent.from_dict(message_data)
                print(f"Received message: {alert_event}")
                send_email(str(alert_event))
                receiver.complete_message(msg)

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
