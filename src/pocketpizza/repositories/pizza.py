from sqlalchemy import select

from pocketpizza import model, schemas
from pocketpizza.dependencies import db


class PizzaRepository:
    def __init__(self, session: db.DatabaseSession):
        self._session = session

    def get_all_pizzas(self):
        return [
            schemas.Pizza(name=p.name, id=p.pizza_id)
            for p in self._session.scalars(select(model.Pizza)).all()
        ]
