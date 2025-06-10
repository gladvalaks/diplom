import datetime
from ..db import Base
from sqlalchemy.orm import mapped_column, Mapped

from backend.use_cases.dto import client

class Client(Base):
    __tablename__ = 'clients'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    deleted_at: Mapped[datetime.datetime | None] = mapped_column(nullable=True)

    def dto(self):
        return client.Client(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            deleted_at=self.deleted_at
        )