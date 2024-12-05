from fastapi import APIRouter, HTTPException

from pocketpizza.schemas import CreateOrder, Order

from pocketpizza.dependencies import repository as repo

router = APIRouter(tags=["order"])

# TODO: 1.1
#       Implement GET /order. We'll need one optional query parameter: user_id. If given, we want to return only the
#       orders for that user.
#
#       For this assignment we'll need the Order Repository to retrieve orders from the database. The order repository
#       has been implemented for you in pocketpizza/repositories/order.py We'll need to turn this into a FastAPI
#       Dependency, which we can then receive in the path operation parameters.

@router.get("/order")
def get_orders(
    # TODO: create a dependency for the OrderRepository class and use it here
    order_repository: repo.OrderRepositoryDependency, 
    user_id: int | None = None
) -> list[Order]:
    return order_repository.get_orders(user_id)


@router.get("/order/{order_id}")
def get_order_by_id(order_id: int, order_repository: repo.OrderRepositoryDependency):
    order = order_repository.get_order_by_id(order_id)

    if order is None:
        raise HTTPException(status_code=404)


@router.post("/order")
def create_order(
    order: CreateOrder, user_id: int, order_repository: repo.OrderRepositoryDependency
):
    order_repository.create_order(order, user_id)
