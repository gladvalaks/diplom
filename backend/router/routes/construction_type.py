import fastapi
from backend.database.db import get_session
from backend.router.deps.token import get_user_id_from_decrypt_access_token
from backend.router.requests.construction_type import PutType
from backend.router.responses.construction_type import ConstructionType
from sqlalchemy.orm import Session
import backend.use_cases.construction_type as use_cases

router = fastapi.APIRouter(dependencies=[fastapi.Depends(get_user_id_from_decrypt_access_token)])

@router.post("/api/construction-types", response_model=ConstructionType)
def create(
    type: PutType,
    session: Session = fastapi.Depends(get_session),
):
    return use_cases.create(
        type=type.type,
        session=session,
    )

@router.get("/api/construction-types", response_model=list[ConstructionType])
def get(
    with_deleted: fastapi.Query[bool],
    session: Session = fastapi.Depends(get_session),
):
    return use_cases.get_all(with_deleted=with_deleted, session=session)

@router.get("/api/construction-types/{construction_type_id}", response_model=list[ConstructionType])
def get_by_id(
    construction_type_id: int,
    session: Session = fastapi.Depends(get_session),
):
    return use_cases.get_by_id(id=construction_type_id, session=session)