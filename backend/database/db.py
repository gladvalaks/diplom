from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, DeclarativeBase

class Base(DeclarativeBase):
    pass


engine = create_engine('postgresql://admin:admin@localhost:1546/crm')

Session = sessionmaker(engine)

def create_db():
    Base.metadata.create_all(engine)


def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()