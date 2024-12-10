from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException

from pocketpizza import schemas
from pocketpizza.repositories import pizza
from pocketpizza.dependencies import user

router = APIRouter(tags=["pizza"])

PizzaRepositoryDependency = Annotated[
    pizza.PizzaRepository, Depends(pizza.PizzaRepository)
]


@router.get("/pizza")
def get_all_pizzas(
    pizza_repository: PizzaRepositoryDependency, current_user: user.CurrentUser
) -> list[schemas.Pizza]:
    return pizza_repository.get_all_pizzas()


@router.get("/pizza/{pizza_id}")
def get_pizza_by_id(
    pizza_id: int,
    pizza_repository: PizzaRepositoryDependency,
    current_user: user.CurrentUser,
) -> schemas.Pizza | None:
    pizza = pizza_repository.get_pizza_by_id(pizza_id)

    if pizza is None:
        raise HTTPException(status_code=404, detail="pizza not found")

    return pizza


@router.post("/pizza")
def create_pizza(
    pizza: schemas.CreatePizza,
    pizza_repository: PizzaRepositoryDependency,
    super_user: user.SuperUser,
) -> schemas.Pizza:
    return pizza_repository.create_pizza(pizza)


@router.put("/pizza/{pizza_id}")
def update_pizza(
    pizza_id: int,
    pizza: schemas.UpdatePizza,
    pizza_repository: PizzaRepositoryDependency,
    super_user: user.SuperUser,
) -> schemas.Pizza | None:
    updated_pizza = pizza_repository.update_pizza(pizza_id, pizza)

    if not updated_pizza:
        raise HTTPException(status_code=404, detail="pizza not found")

    return updated_pizza
