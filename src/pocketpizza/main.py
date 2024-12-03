from contextlib import asynccontextmanager
from fastapi import FastAPI

from pocketpizza import database
from pocketpizza.api import order, pizza, user


@asynccontextmanager
async def lifespan(app: FastAPI):
    database.create()
    database.seed()

    yield


app = FastAPI(lifespan=lifespan)
app.include_router(order.router)
app.include_router(pizza.router)
# app.include_router(user.router)
