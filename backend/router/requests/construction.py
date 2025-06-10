import decimal
import pydantic

class PutConstruction(pydantic.BaseModel):
    description: str
    client_id: int
    construction_type_id: int
    contractor_id: int
    price: decimal.Decimal