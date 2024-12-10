from fastapi import FastAPI

from pocketpizza.api import order, pizza, user
from pocketpizza.lifespan import lifespan


app = FastAPI(lifespan=lifespan)
app.include_router(order.router)
app.include_router(pizza.router)

# TODO: uncomment for Exercise 2
app.include_router(user.router)
