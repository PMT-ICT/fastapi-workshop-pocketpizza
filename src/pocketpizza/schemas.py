from pydantic import BaseModel


class PizzaBase(BaseModel):
    name: str


class CreatePizza(PizzaBase):
    pass


class UpdatePizza(PizzaBase):
    id: int | None = None


class Pizza(PizzaBase):
    id: int


class OrderBase(BaseModel):
    order_id: int


class CreateOrder(OrderBase):
    pizza_ids: list[int]


class Order(OrderBase):
    pizzas: list[Pizza]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: int


class Address(BaseModel):
    street: str
    house_number: int
