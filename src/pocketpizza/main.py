from fastapi import FastAPI

from pocketpizza.api import order, user
from pocketpizza.lifespan import lifespan


app = FastAPI(lifespan=lifespan)
app.include_router(order.router)

# TODO: uncomment for Exercise 2
# app.include_router(user.router)

# TODO: uncomment for Bonus Exercise
# from pocketpizza.api import pizza
# app.include_router(pizza.router)
