import datetime
import decimal
import backend.database.entities.construction as construction
from sqlalchemy.orm import Session
import sqlalchemy as sa

def create(
        description: str,
        client_id: int,
        construction_type_id: int,
        contractor_id: int,
        price: decimal.Decimal,
        session: Session,
    ):
    created_construction = construction.Construction(
        description=description,
        client_id=client_id,
        construction_type_id=construction_type_id,
        contractor_id=contractor_id,
        price=price
    )
    session.add(created_construction)
    
    return created_construction.dto()

def get_all(with_deleted: bool, session: Session):
    if (with_deleted):
        query = sa.select(construction.Construction)
    else:
        query = sa.select(construction.Construction).filter_by(deleted_at=None)

    return [ct.dto() for ct in session.scalars(query).all()]

def get_by_id(id: int, session: Session):
    result = session.scalars(sa.select(construction.Construction).filter_by(id=id)).one_or_none()
    if result:
        return result.dto()
    
    return result

def delete(id: int, session: Session):
    construction_to_delete = session.scalars(sa.select(construction.Construction).filter_by(id=id)).one_or_none()
    
    if construction_to_delete is None:
        return None
    
    construction_to_delete.deleted_at = datetime.datetime.now()
    
    return construction_to_delete.dto()

def undelete(id: int, session: Session):
    construction_to_undelete = session.scalars(sa.select(construction.Construction).filter_by(id=id)).one_or_none()
    
    if construction_to_undelete is None:
        return None
    
    construction_to_undelete.deleted_at = None
    
    return construction_to_undelete.dto()