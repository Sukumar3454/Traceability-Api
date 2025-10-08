from pydantic import BaseModel, Field
from typing import Literal

class NotificationCreate(BaseModel):
    entity_type: Literal["Candidate", "Requirement", "Vendor", "Lead", "Case"] = Field(..., example="Case")
    entity_id: int = Field(..., example=101)
    message: str = Field(..., example="New email received")
