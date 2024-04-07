from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from config_bd.BaseModel import Users, Users_profile


async def orm_add_user(session: AsyncSession, telegram_id, first_name, user_name):
    obj = Users(
        telegram_id=telegram_id,
        first_name=first_name,
        user_name=user_name,
    )
    session.add(obj)
    await session.commit()


async def orm_add_user_profile(session: AsyncSession, telegram_id):
    obj = Users_profile(
        telegram_id=telegram_id,
    )
    session.add(obj)
    await session.commit()


async def orm_select_user_profile(session: AsyncSession, telegram_id: str):
    query = select(Users_profile).where(Users_profile.telegram_id == telegram_id)
    result = await session.execute(query)
    return result.scalars().one()
