from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException

from pocketpizza.schemas import CreateOrder, Order
from pocketpizza.repositories import order
from pocketpizza.dependencies.user import CurrentUser

router = APIRouter(tags=["order"])

# TODO: Exercise 1.1
OrderRepositoryDependency = Annotated[
    order.OrderRepository, Depends(order.OrderRepository)
]


# TODO: Exercise 1.2
# TODO: Exercise 2.2
@router.get("/order")
def get_orders(
    # TODO: create a dependency for the OrderRepository class and use it here
    order_repository: OrderRepositoryDependency,
    current_user: CurrentUser
    
) -> list[Order]:
    # TODO: return list of orders from the order repository
    return order_repository.get_orders(current_user.user_id)


# TODO: Exercise 1.3
# TODO: Exercise 2.3
@router.get("/order/{order_id}")
def get_order_by_id(order_id: int, order_repository: OrderRepositoryDependency):
    order = order_repository.get_order_by_id(order_id)

    if order is None:
        raise HTTPException(status_code=404)


# TODO: Exercise 1.4
# TODO: Exercise 2.3
@router.post("/order")
def create_order(order: CreateOrder, order_repository: OrderRepositoryDependency):
    return order_repository.create_order(order)
