from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from pocketpizza.database import engine


def get_db():
    try:
        session = Session(engine)
        yield session
    finally:
        session.close()


DatabaseSession = Annotated[Session, Depends(get_db)]
