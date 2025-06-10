import pydantic
import datetime

class Client(pydantic.BaseModel):
    id: int
    first_name: str
    last_name: str
    deleted_at: datetime.datetime | None