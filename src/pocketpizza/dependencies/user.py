from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from pocketpizza import model, security, settings
from pocketpizza.repositories import user as u

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/login/access-token")


def get_current_user(
    user_repository: Annotated[u.UserRepository, Depends(u.UserRepository)],
    token: str = Depends(reusable_oauth2),
):
    user_id = security.get_user_id_from_token(token)
    user = user_repository.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


CurrentUser = Annotated[model.User, Depends(get_current_user)]


def get_current_superuser(
    current_user: model.User = Depends(get_current_user),
):
    if not current_user.email == settings.super_user_email:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not the superuser"
        )
    return current_user


SuperUser = Annotated[model.User, Depends(get_current_superuser)]
