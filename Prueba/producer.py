from Infrastructure.Gestor_de_Colas.Azure.Azure import send_message
from EventProducer.Domain.Alert_Event import AlertEvent

if __name__ == "__main__":
    alert_event = AlertEvent(
        alert_id="1",
        alert_message="Hola, este es un mensaje de prueba por correo electrónico",
        alert_timestamp="2024-06-14T12:00:00Z"
    )
    send_message(alert_event)
