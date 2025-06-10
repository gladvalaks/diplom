import datetime
import decimal
from ..db import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey

from backend.use_cases.dto import construction

class Construction(Base):
    __tablename__ = 'constructions'

    id: Mapped[int] = mapped_column(primary_key=True)

    description: Mapped[str] = mapped_column(nullable=False)
    client_id: Mapped[int] = mapped_column(ForeignKey('clients.id'), nullable=False)
    construction_type_id: Mapped[int] = mapped_column(ForeignKey('construction_types.id'), nullable=False)
    contractor_id: Mapped[int] = mapped_column(ForeignKey('contractors.id'), nullable=False)
    deleted_at: Mapped[datetime.datetime | None] = mapped_column(nullable=True)
    price: Mapped[decimal.Decimal] = mapped_column(nullable=False)

    def dto(self):
        return construction.Construction(
            id=self.id,
            description=self.description,
            client_id=self.client_id,
            construction_type_id=self.construction_type_id,
            contractor_id=self.contractor_id,
            deleted_at=self.deleted_at,
            price=self.price,
        )