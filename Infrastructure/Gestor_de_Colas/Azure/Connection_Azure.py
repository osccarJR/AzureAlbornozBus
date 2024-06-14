import json
from azure.servicebus import ServiceBusClient

# Leer las credenciales desde el archivo credentials.json
with open('Prueba/credentials.json', 'r') as f:
    credentials = json.load(f)

CONNECTION_STR = credentials["connection_string"]
QUEUE_NAME = credentials["queue_name"]

def get_servicebus_client():
    return ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)
