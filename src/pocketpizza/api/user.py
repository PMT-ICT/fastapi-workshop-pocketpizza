from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from pocketpizza import schemas, security
from pocketpizza.repositories import user as u

router = APIRouter()


@router.post("/login/access-token", response_model=schemas.Token)
def login_access_token(
    user_repository: u.UserRepositoryDependency,
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    """
    OAuth2 compatible token login, get an access token for future requests.
    """
    user = user_repository.authenticate_user(
        email=form_data.username, password=form_data.password
    )

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    return {
        "access_token": security.create_access_token(subject=str(user.user_id)),
        "token_type": "bearer",
    }
