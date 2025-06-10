import pydantic

class PutClient(pydantic.BaseModel):
    first_name: str
    last_name: str
