from fastapi import APIRouter

from pocketpizza import schemas
from pocketpizza.dependencies import repository as repo

router = APIRouter(tags=["pizza"])


@router.get("/pizza")
def get_all_pizzas(
    pizza_repository: repo.PizzaRepositoryDependency,
) -> list[schemas.Pizza]:
    return pizza_repository.get_all_pizzas()
