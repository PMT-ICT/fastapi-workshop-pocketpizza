from typing import Annotated
from fastapi import APIRouter, Depends

from pocketpizza.repositories import order

router = APIRouter(tags=["order"])

# TODO: Exercise 1.1
OrderRepositoryDependency = Annotated[
    order.OrderRepository, Depends(order.OrderRepository)
]


# TODO: Exercise 1.2
# TODO: Exercise 2.2
...

# TODO: Exercise 1.3
# TODO: Exercise 2.3
...

# TODO: Exercise 1.4
# TODO: Exercise 2.3
...
