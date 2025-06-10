import fastapi
from backend.database.db import get_session
from backend.router.deps.token import get_user_id_from_decrypt_access_token
from backend.router.requests.client import PutClient
from sqlalchemy.orm import Session
import backend.use_cases.client as use_cases

router = fastapi.APIRouter(dependencies=[fastapi.Depends(get_user_id_from_decrypt_access_token)])

@router.post("/api/tasks")
def create_client(
    client: PutClient,
    session: Session = fastapi.Depends(get_session),
):
    return use_cases.create(
        first_name=client.first_name,
        last_name=client.last_name,
        session=session,
    )
