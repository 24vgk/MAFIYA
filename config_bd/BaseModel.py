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
    on_off: Mapped[bool] = mapped_column(default=True)


# class SumConstant(Base):
#     __tablename__ = 'Sum_constant'
#
#     id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, unique=True)
#     sum_gold: Mapped[int] = mapped_column(default=100)
#     count_stones: Mapped[int] = mapped_column(default=1)
#     stones1: Mapped[int] = mapped_column(default=40)
#     stones2: Mapped[int] = mapped_column(default=80)
#     stones5: Mapped[int] = mapped_column(default=180)
#     stones10: Mapped[int] = mapped_column(default=300)
#     sum_protection: Mapped[int] = mapped_column(default=100)
#     sum_documents: Mapped[int] = mapped_column(default=150)
#     sum_antivirus: Mapped[int] = mapped_column(default=150)
#     sum_active_role: Mapped[int] = mapped_column(default=1)
#     sum_bullet: Mapped[int] = mapped_column(default=1)
