class AlertEvent:
    def __init__(self, alert_id, alert_message, alert_timestamp):
        self.alert_id = alert_id
        self.alert_message = alert_message
        self.alert_timestamp = alert_timestamp

    def to_dict(self):
        return {
            "alert_id": self.alert_id,
            "alert_message": self.alert_message,
            "alert_timestamp": self.alert_timestamp
        }

    @staticmethod
    def from_dict(data):
        return AlertEvent(
            alert_id=data.get("alert_id"),
            alert_message=data.get("alert_message"),
            alert_timestamp=data.get("alert_timestamp")
        )

    def __str__(self):
        return f"AlertEvent(alert_id={self.alert_id}, alert_message={self.alert_message}, alert_timestamp={self.alert_timestamp})"
