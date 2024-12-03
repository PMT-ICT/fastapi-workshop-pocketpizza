import random
from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from pocketpizza import settings
from pocketpizza.model import Base, User, Order, Pizza

from pocketpizza.repositories import user as u


def seed():
    with Session(engine) as session:
        user_repository = u.UserRepository(session)

        if any(session.scalars(select(User))):
            return

        for user_name in (
            "elfrayline",
            "quincy",
            "ricardo",
            "kevin",
            "ramphison",
            "nathaniel",
        ):
            user_repository.create_user(f"{user_name}@pocketpizza.com", "swordfish")

        user_repository.create_user("superuser@pocketpizza.com", "shoarmapizza")

        users = session.scalars(
            select(User).where(User.email.not_like(settings.super_user_email))
        ).all()

        pizzas = [
            Pizza(name=pizza_name)
            for pizza_name in (
                "Margherita",
                "Quattro Stagioni",
                "Quattro Formaggi",
                "Napoletana",
                "Calzone",
                "Tricolore",
            )
        ]

        session.add_all(pizzas)

        for user in users:
            session.add_all(
                (
                    Order(
                        user_id=user.user_id,
                        pizzas=[random.choice(pizzas) for _ in range(5)],
                    )
                    for _ in range(2)
                )
            )

        session.commit()


def create():
    Base.metadata.create_all(engine)


engine = create_engine(settings.sqlalchemy_url, echo=True)


def get_db():
    try:
        session = Session(engine)
        yield session
    finally:
        session.close()


DatabaseSession = Annotated[Session, Depends(get_db)]
