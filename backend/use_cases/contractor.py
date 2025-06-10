import datetime
import decimal
import backend.database.entities.contractor as contractor
from sqlalchemy.orm import Session
import sqlalchemy as sa

def create(
        first_name: str,
        last_name: str,
        percentage: decimal.Decimal,
        session: Session,
    ):
    created_contractor = contractor.Contractor(
        first_name=first_name,
        last_name=last_name,
        percentage=percentage,
    )
    session.add(created_contractor)
    
    return created_contractor.dto()

def get_all(with_deleted: bool, session: Session):
    if (with_deleted):
        query = sa.select(contractor.Contractor)
    else:
        query = sa.select(contractor.Contractor).filter_by(deleted_at=None)

    return [ct.dto() for ct in session.scalars(query).all()]

def get_by_id(id: int, session: Session):
    result = session.scalars(sa.select(contractor.Contractor).filter_by(id=id)).one_or_none()
    if result:
        return result.dto()
    
    return result

def delete(id: int, session: Session):
    contractor_to_delete = session.scalars(sa.select(contractor.Contractor).filter_by(id=id)).one_or_none()
    
    if contractor_to_delete is None:
        return None
    
    contractor_to_delete.deleted_at = datetime.datetime.now()
    
    return contractor_to_delete.dto()

def undelete(id: int, session: Session):
    contractor_to_undelete = session.scalars(sa.select(contractor.Contractor).filter_by(id=id)).one_or_none()
    
    if contractor_to_undelete is None:
        return None
    
    contractor_to_undelete.deleted_at = None
    
    return contractor_to_undelete.dto()