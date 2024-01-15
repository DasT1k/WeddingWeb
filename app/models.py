from app import db
from typing import Optional
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

class Quest(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), index=True)
    zags: Mapped[bool] = mapped_column(Boolean())
    drink: Mapped[Optional[str]] = mapped_column(String(80))
    food: Mapped[str] = mapped_column(String(5))

    def __repr__(self):
        return f"{self.id:<3} | {self.name:<40} | {self.zags} | {self.drink:<40} | {self.food}" # TODO: не работает форматирование ширины элементов