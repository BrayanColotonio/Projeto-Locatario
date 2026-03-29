from pydantic import BaseModel

class vehicle(BaseModel):
    id: int
    name: str
    brand: str
    year: int