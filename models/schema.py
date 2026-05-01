from pydantic import BaseModel
from typing import List, Optional

class PatientRecord(BaseModel):
    symptoms: List[str]
    duration: str
    medication: Optional[str] = None
    risk_level: Optional[str] = None
