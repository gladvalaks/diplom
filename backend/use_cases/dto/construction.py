import datetime
import decimal
import pydantic

class Construction(pydantic.BaseModel):
    id: int
    description: str
    client_id: int
    construction_type_id: int
    contractor_id: int
    deleted_at: datetime.datetime | None
    price: decimal.Decimal