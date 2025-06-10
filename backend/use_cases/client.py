import datetime
import backend.database.entities.client as client
from sqlalchemy.orm import Session
import sqlalchemy as sa

def create(first_name: str, last_name: str, session: Session):
    created_client = client.Client(
        first_name=first_name,
        last_name=last_name,
        deleted_at=None,
    )
    session.add(created_client)
    
    return created_client.dto()

def get_all(with_deleted: bool, session: Session):
    if (with_deleted):
        query = sa.select(client.Client)
    else:
        query = sa.select(client.Client).filter_by(deleted_at=None)

    return [ct.dto() for ct in session.scalars(query).all()]

def get_by_id(id: int, session: Session):
    result = session.scalars(sa.select(client.Client).filter_by(id=id)).one_or_none()
    if result:
        return result.dto()
    
    return result

def delete(id: int, session: Session):
    client_to_delete = session.scalars(sa.select(client.Client).filter_by(id=id)).one_or_none()
    
    if client_to_delete is None:
        return None
    
    client_to_delete.deleted_at = datetime.datetime.now()
    
    return client_to_delete.dto()

def undelete(id: int, session: Session):
    client_to_undelete = session.scalars(sa.select(client.Client).filter_by(id=id)).one_or_none()
    
    if client_to_undelete is None:
        return None
    
    client_to_undelete.deleted_at = None
    
    return client_to_undelete.dto()