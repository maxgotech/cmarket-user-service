from sqlalchemy.orm import Mapped, mapped_column
from app import db


class UserModel(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    mail: Mapped[str]

    def __repr__(self) -> str:
        return f"User(name = {self.name}, mail = {self.mail})"
