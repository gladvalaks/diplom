import pydantic

import decimal

class PutContractor(pydantic.BaseModel):
    first_name: str
    last_name: str
    percentage: decimal.Decimal