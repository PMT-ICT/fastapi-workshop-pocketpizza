from __future__ import annotations
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    orders: Mapped[list[Order]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


order_pizza_association_table = Table(
    "order_pizza_association_table",
    Base.metadata,
    Column("order_pizza_id", Integer, primary_key=True),
    Column("order_id", ForeignKey("order.order_id")),
    Column("pizza_id", ForeignKey("pizza.pizza_id")),
)


class Order(Base):
    __tablename__ = "order"

    order_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"))
    user: Mapped[User] = relationship(back_populates="orders")

    pizzas: Mapped[list[Pizza]] = relationship(secondary=order_pizza_association_table)


class Pizza(Base):
    __tablename__ = "pizza"

    pizza_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
