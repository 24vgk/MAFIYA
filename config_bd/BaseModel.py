from sqlalchemy import DateTime, Float, String, Text, func, ForeignKey, PrimaryKeyConstraint, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), server_onupdate=func.now())


class Users(Base):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(nullable=True, autoincrement=True, primary_key=True, unique=True)
    telegram_id: Mapped[str] = mapped_column(String(20), primary_key=True, nullable=True, unique=True)
    first_name: Mapped[str] = mapped_column(String(100))
    user_name: Mapped[float] = mapped_column(String(50))


class Users_profile(Base):
    __tablename__ = 'Users_profile'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, unique=True)
    telegram_id: Mapped[str] = mapped_column(String(20), ForeignKey("Users.telegram_id", ondelete="CASCADE", onupdate="CASCADE"), nullable=True, unique=True)
    gold: Mapped[int] = mapped_column(Integer, default=0)
    stones: Mapped[int] = mapped_column(default=0)
    protection: Mapped[int] = mapped_column(default=0)
    documents: Mapped[int] = mapped_column(default=0)
    antivirus: Mapped[int] = mapped_column(default=0)
    active_role: Mapped[int] = mapped_column(default=0)
    bullet: Mapped[int] = mapped_column(default=0)

