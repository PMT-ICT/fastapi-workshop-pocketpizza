from sqlalchemy import select
from pocketpizza import model, schemas, database


class OrderRepository:
    def __init__(self, session: database.DatabaseSession):
        self._session = session

    def get_orders(self, user_id: int | None):
        query = select(model.Order)

        if user_id:
            query = query.where(model.Order.user_id == user_id)

        result = self._session.scalars(query).all()

        return [
            schemas.Order(
                order_id=order.order_id,
                pizzas=[
                    schemas.Pizza(name=pizza.name, id=pizza.pizza_id)
                    for pizza in order.pizzas
                ],
            )
            for order in result
        ]

    def get_order_by_id(self, order_id: int) -> schemas.Order | None:
        query = select(model.Order).where(model.Order.order_id == order_id)
        order = self._session.scalar(query)

        return (
            schemas.Order(
                order_id=order.order_id,
                pizzas=[
                    schemas.Pizza(name=pizza.name, id=pizza.pizza_id)
                    for pizza in order.pizzas
                ],
            )
            if order
            else None
        )
