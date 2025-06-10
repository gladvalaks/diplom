import datetime
import pydantic

class ConstructionType(pydantic.BaseModel):
    id: int
    type: str
    deleted_at: datetime.datetime | None