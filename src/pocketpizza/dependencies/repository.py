from typing import Annotated

from fastapi import Depends
from pocketpizza.repositories import order, pizza, user

OrderRepositoryDependency = Annotated[
    order.OrderRepository, Depends(order.OrderRepository)
]

PizzaRepositoryDependency = Annotated[
    pizza.PizzaRepository, Depends(pizza.PizzaRepository)
]

UserRepositoryDependency = Annotated[user.UserRepository, Depends(user.UserRepository)]
