import pydantic

class AuthUser(pydantic.BaseModel):
    login: str
    password: str