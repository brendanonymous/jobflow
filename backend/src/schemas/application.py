from pydantic import BaseModel, ConfigDict
from datetime import date, datetime

class ApplicationCreateRequest(BaseModel):
    company_name:   str
    role_name:      str
    applied_date: date | None = None

class ApplicationCreateResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_name: str
    role_name: str
    applied_date: date
    created_at: datetime