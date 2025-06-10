import datetime
import pydantic

import decimal

class Contractor(pydantic.BaseModel):
    id: int
    first_name: str
    last_name: str
    percentage: decimal.Decimal
    deleted_at: datetime.datetime | None
