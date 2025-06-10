import pydantic

class User(pydantic.BaseModel):
    id: int
    name: str
    login: str
    password: str