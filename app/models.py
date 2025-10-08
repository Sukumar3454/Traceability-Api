from datetime import datetime

VALID_ENTITIES = ["Candidate", "Requirement", "Vendor", "Lead", "Case"]

class Notification:
    def __init__(self, entity_type: str, entity_id: int, message: str):
        if entity_type not in VALID_ENTITIES:
            raise ValueError(f"Invalid entity type: {entity_type}. Must be one of {VALID_ENTITIES}")

        # Ensure the message mentions the entity
        if entity_type not in message:
            message = f"{message} on {entity_type} {entity_id}"

        self.entity_type = entity_type
        self.entity_id = entity_id
        self.message = message
        self.timestamp = datetime.now().isoformat()

    def to_dict(self):
        return {
            "entity_type": self.entity_type,
            "entity_id": self.entity_id,
            "message": self.message,
            "timestamp": self.timestamp
        }
