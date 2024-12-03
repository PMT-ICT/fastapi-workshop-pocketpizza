from typing import Annotated
from fastapi import Depends

from pocketpizza import model, security, database


class UserRepository:
    def __init__(self, session: database.DatabaseSession):
        self._session = session

    def get_user(self, user_id: int):
        return (
            self._session.query(model.User)
            .filter(model.User.user_id == user_id)
            .first()
        )

    def get_user_by_email(self, email: str):
        return (
            self._session.query(model.User)
            .filter(model.User.email == email)
            .first()
        )

    def get_users(self, skip: int = 0, limit: int = 100):
        return self._session.query(model.User).offset(skip).limit(limit).all()

    def create_user(self, email: str, password: str):
        hashed_password = security.get_password_hash(password)
        db_user = model.User(email=email, hashed_password=hashed_password)
        self._session.add(db_user)
        self._session.commit()
        self._session.refresh(db_user)
        return db_user

    def authenticate_user(self, email: str, password: str):
        user = self.get_user_by_email(email=email)
        if not user:
            return None
        if not security.verify_password(password, user.hashed_password):
            return None
        return user


UserRepositoryDependency = Annotated[UserRepository, Depends(UserRepository)]
