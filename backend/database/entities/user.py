from ..db import Base
from sqlalchemy.orm import mapped_column, Mapped

from backend.use_cases.dto import user

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    login: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)

    def dto(self):
        return user.User(
            id=self.id,
            name=self.name,
            login=self.login,
            password=self.password,
        )