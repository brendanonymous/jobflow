from pydantic import BaseModel
from enum import Enum

class Status(str, Enum):
    APPLIED = "Applied"
    INTERVIEW = "Interview"
    OFFER = "Offer"
    REJECTED = "Rejected"
    WITHDRAWN = "Withdrawn"
    GHOSTED = "Ghosted"

class StatusEventCreateRequest(BaseModel):
    status:   Status

