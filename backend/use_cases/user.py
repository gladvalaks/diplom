import datetime
import backend.database.entities.user as user
from sqlalchemy.orm import Session
import sqlalchemy as sa

def get_by_user_login_and_password(login: str, password: str, session: Session):
    result = session.scalars(
            sa.select(user.User).filter_by(login=login, password=password)
        ).one_or_none()
    if result:
        return result.dto()
    
    return result