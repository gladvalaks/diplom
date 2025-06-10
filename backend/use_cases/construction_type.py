import datetime
import backend.database.entities.construction_type as construction_type
from sqlalchemy.orm import Session
import sqlalchemy as sa

def create(type: str, session: Session):
    created_construction_type = construction_type.ConstructionType(
        type=type,
        deleted_at=None,
    )
    session.add(created_construction_type)
    
    return created_construction_type.dto()

def get_all(with_deleted: bool, session: Session):
    if (with_deleted):
        query = sa.select(construction_type.ConstructionType)
    else:
        query = sa.select(construction_type.ConstructionType).filter_by(deleted_at=None)

    return [ct.dto() for ct in session.scalars(query).all()]

def get_by_id(id: int, session: Session):
    result = session.scalars(sa.select(construction_type.ConstructionType).filter_by(id=id)).one_or_none()
    if result:
        return result.dto()
    
    return result

def delete(id: int, session: Session):
    construction_type_to_delete = session.scalars(sa.select(construction_type.ConstructionType).filter_by(id=id)).one_or_none()
    
    if construction_type_to_delete is None:
        return None
    
    construction_type_to_delete.deleted_at = datetime.datetime.now()
    
    return construction_type_to_delete.dto()

def undelete(id: int, session: Session):
    construction_type_to_undelete = session.scalars(sa.select(construction_type.ConstructionType).filter_by(id=id)).one_or_none()
    
    if construction_type_to_undelete is None:
        return None
    
    construction_type_to_undelete.deleted_at = None
    
    return construction_type_to_undelete.dto()