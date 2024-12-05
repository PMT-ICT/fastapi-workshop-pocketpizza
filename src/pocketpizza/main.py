from fastapi import FastAPI

from pocketpizza.api import order, pizza
from pocketpizza.lifespan import lifespan


app = FastAPI(lifespan=lifespan)
app.include_router(order.router)
app.include_router(pizza.router)

# TODO: uncomment for last exercise
# app.include_router(user.router)
