from sqlalchemy import select

from pocketpizza import model, schemas
from pocketpizza.dependencies import db


class PizzaRepository:
    def __init__(self, session: db.DatabaseSession):
        self._session = session

    def get_all_pizzas(self) -> list[schemas.Pizza]:
        return [
            schemas.Pizza(name=p.name, id=p.pizza_id)
            for p in self._session.scalars(select(model.Pizza)).all()
        ]

    def get_pizza_by_id(self, pizza_id: int) -> schemas.Pizza | None:
        pizza = self._session.scalar(
            select(model.Pizza).where(model.Pizza.pizza_id == pizza_id)
        )

        return schemas.Pizza(name=pizza.name, id=pizza.pizza_id) if pizza else None

    def create_pizza(self, pizza: schemas.CreatePizza) -> schemas.Pizza:
        new_pizza = model.Pizza(name=pizza.name)
        self._session.add(new_pizza)
        self._session.commit()

        return schemas.Pizza(name=new_pizza.name, id=new_pizza.pizza_id)

    def update_pizza(
        self, pizza_id: int, pizza: schemas.UpdatePizza
    ) -> schemas.Pizza | None:
        existing_pizza = self._session.scalar(
            select(model.Pizza).where(model.Pizza.pizza_id == pizza_id)
        )

        if existing_pizza:
            existing_pizza.name = pizza.name
            self._session.commit()

            return schemas.Pizza(name=existing_pizza.name, id=existing_pizza.pizza_id)
