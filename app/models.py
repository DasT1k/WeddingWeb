from typing import Optional
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class Quest(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), index=True)
    zags: Mapped[bool] = mapped_column(Boolean())
    drink: Mapped[Optional[str]] = mapped_column(String(80))
    food: Mapped[str] = mapped_column(String(5))
