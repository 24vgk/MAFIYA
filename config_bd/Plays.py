from sqlalchemy import select, update, delete
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from config_bd.BaseModel import Plays


async def add_play(session: AsyncSession, user, group):
    obj = Plays(
        group=group,
        user1=user
    )
    session.add(obj)
    await session.commit()


async def select_play_user(session: AsyncSession, user, group):
    stmt = select(Plays).where(Plays.user1 == user, Plays.group == group)
    result = await session.execute(stmt)
    return result.scalars().all()


async def update_users_game(session: AsyncSession, user, play_id, position):
    query = select(Plays).where(Plays.play_id == play_id)
    res = await session.execute(query)
    if user in res.scalars().all():
        print(res.scalars().all())