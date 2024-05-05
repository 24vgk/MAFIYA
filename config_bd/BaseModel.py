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
    refer: Mapped[str] = mapped_column(String(20), nullable=True)
    bonus: Mapped[int] = mapped_column(default=0)
    is_admin: Mapped[bool] = mapped_column(default=False)


class Users_profile(Base):
    __tablename__ = 'Users_profile'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, unique=True)
    telegram_id: Mapped[str] = mapped_column(String(20),
                                             ForeignKey("Users.telegram_id", ondelete="CASCADE", onupdate="CASCADE"),
                                             nullable=True, unique=True)
    gold: Mapped[int] = mapped_column(default=0)
    stones: Mapped[int] = mapped_column(default=0)
    protection: Mapped[int] = mapped_column(default=0)
    documents: Mapped[int] = mapped_column(default=0)
    antivirus: Mapped[int] = mapped_column(default=0)
    active_role: Mapped[int] = mapped_column(default=0)
    bullet: Mapped[int] = mapped_column(default=0)
    on_off: Mapped[bool] = mapped_column(default=True)


class Users_history_balance(Base):
    __tablename__ = 'Users_history_balance'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, unique=True)
    telegram_id: Mapped[str] = mapped_column(String(20),
                                             ForeignKey("Users.telegram_id", ondelete="CASCADE", onupdate="CASCADE"),
                                             nullable=True)
    type: Mapped[int] = mapped_column(String(100))
    comment: Mapped[int] = mapped_column(String(100))
    sum: Mapped[int] = mapped_column()


class Users_history_play(Base):
    __tablename__ = 'Users_history_play'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, unique=True)
    telegram_id: Mapped[str] = mapped_column(String(20),
                                             ForeignKey("Users.telegram_id", ondelete="CASCADE", onupdate="CASCADE"),
                                             nullable=True)
    type: Mapped[int] = mapped_column(String(100))
    comment: Mapped[int] = mapped_column(String(100))
    num_play: Mapped[int] = mapped_column()


class Plays(Base):
    __tablename__ = 'Plays'

    play_id: Mapped[int] = mapped_column(nullable=True, autoincrement=True, primary_key=True, unique=True)
    group: Mapped[str] = mapped_column(String(50), default='-')
    user1: Mapped[str] = mapped_column(String(50), default='-')
    user2: Mapped[str] = mapped_column(String(50), default='-')
    user3: Mapped[str] = mapped_column(String(50), default='-')
    user4: Mapped[str] = mapped_column(String(50), default='-')
    user5: Mapped[str] = mapped_column(String(50), default='-')
    user6: Mapped[str] = mapped_column(String(50), default='-')
    user7: Mapped[str] = mapped_column(String(50), default='-')
    user8: Mapped[str] = mapped_column(String(50), default='-')
    user9: Mapped[str] = mapped_column(String(50), default='-')
    user10: Mapped[str] = mapped_column(String(50), default='-')
    user11: Mapped[str] = mapped_column(String(50), default='-')
    user12: Mapped[str] = mapped_column(String(50), default='-')
    user13: Mapped[str] = mapped_column(String(50), default='-')
    user14: Mapped[str] = mapped_column(String(50), default='-')
    user15: Mapped[str] = mapped_column(String(50), default='-')
    user16: Mapped[str] = mapped_column(String(50), default='-')
    user17: Mapped[str] = mapped_column(String(50), default='-')
    user18: Mapped[str] = mapped_column(String(50), default='-')


class Plays_history(Base):
    __tablename__ = 'Plays_history'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, unique=True)
    play_id: Mapped[str] = mapped_column(String(20),
                                         ForeignKey("Users.telegram_id", ondelete="CASCADE", onupdate="CASCADE"),
                                         nullable=True, unique=True)
    telegram_id_create: Mapped[str] = mapped_column(String(20))
    type: Mapped[int] = mapped_column(String(100))
    comment: Mapped[int] = mapped_column(String(100))
    win_user: Mapped[str] = mapped_column(String(50))

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
