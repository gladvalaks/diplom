import fastapi
from backend.database.db import get_session
from backend.router.deps.token import get_user_id_from_decrypt_access_token
from backend.router.requests.client import PutClient
from backend.router.responses.client import Client
from sqlalchemy.orm import Session
import backend.use_cases.client as use_cases

router = fastapi.APIRouter(dependencies=[fastapi.Depends(get_user_id_from_decrypt_access_token)])

@router.post("/api/clients", response_model=Client)
def create(
    client: PutClient,
    session: Session = fastapi.Depends(get_session),
):
    return use_cases.create(
        first_name=client.first_name,
        last_name=client.last_name,
        session=session,
    )

@router.get("/api/clients", response_model=list[Client])
def get(
    with_deleted: fastapi.Query[bool],
    session: Session = fastapi.Depends(get_session),
):
    return use_cases.get_all(with_deleted=with_deleted, session=session)

@router.get("/api/clients/{client_id}", response_model=list[Client])
def get_by_id(
    client_id: int,
    session: Session = fastapi.Depends(get_session),
):
    return use_cases.get_by_id(id=client_id, session=session)