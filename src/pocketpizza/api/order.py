from fastapi import APIRouter, HTTPException

from pocketpizza import deps
from pocketpizza.schemas import Order

from pocketpizza.repositories import order

router = APIRouter()


@router.get("/order")
def get_orders(
    order_repository: order.OrderRepository,
    current_user: deps.CurrentUser,
    all_users=False,
) -> list[Order]:
    return order_repository.get_orders(current_user.user_id if not all_users else None)


@router.get("/order/{order_id}")
def get_order_by_id(
    order_id: int, order_repository: order.OrderRepository, superuser: deps.SuperUser
):
    order = order_repository.get_order_by_id(order_id)

    if order is None:
        raise HTTPException(status_code=404)
