import datetime
from ..db import Base
from sqlalchemy.orm import mapped_column, Mapped

from backend.use_cases.dto import construction_type

class ConstructionType(Base):
    __tablename__ = 'construction_types'

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(nullable=False)
    deleted_at: Mapped[datetime.datetime | None] = mapped_column(nullable=True)

    def dto(self):
        return construction_type.ConstructionType(
            id=self.id,
            type=self.type,
            deleted_at=self.deleted_a
        )