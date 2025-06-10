import fastapi

from backend.database.db import get_session
from backend.router.requests.user import AuthUser
from backend.router.deps.token import create_access_token
from sqlalchemy.orm import Session
from backend.use_cases.user import get_by_user_login_and_password


router = fastapi.APIRouter()

@router.post("/api/login")
def login(
    auth_user: AuthUser,
    response: fastapi.Response,
    session: Session = fastapi.Depends(get_session),
):
    user = get_by_user_login_and_password(
        login=auth_user.login, password=auth_user.password, session=session
    )
    if user:
        response = fastapi.responses.JSONResponse(content={"response": "OK"})
        response.set_cookie(
            key="token",
            value=create_access_token(data={"user_id": user.id}),
            secure=False,
            samesite=None,
        )
        response.status_code = fastapi.status.HTTP_200_OK
        return response
    else:
        response.status_code = fastapi.status.HTTP_422_UNPROCESSABLE_ENTITY