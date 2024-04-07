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


async def orm_update_user_profile_on_off(session: AsyncSession, telegram_id: str, on_off: bool):
    obj = update(Users_profile).where(Users_profile.telegram_id == telegram_id).values(on_off=on_off)
    await session.execute(obj)
    await session.commit()


async def orm_update_user_profile_stones(session: AsyncSession, telegram_id: str, stones: int):
    obj = update(Users_profile).where(Users_profile.telegram_id == telegram_id).values(stones=stones)
    await session.execute(obj)
    await session.commit()


async def orm_update_user_profile_gold(session: AsyncSession, telegram_id: str, gold: int):
    obj = update(Users_profile).where(Users_profile.telegram_id == telegram_id).values(gold=gold)
    await session.execute(obj)
    await session.commit()


async def orm_update_user_profile_protection(session: AsyncSession, telegram_id: str, protection: int):
    obj = update(Users_profile).where(Users_profile.telegram_id == telegram_id).values(protection=protection)
    await session.execute(obj)
    await session.commit()


async def orm_update_user_profile_documents(session: AsyncSession, telegram_id: str, documents: int):
    obj = update(Users_profile).where(Users_profile.telegram_id == telegram_id).values(documents=documents)
    await session.execute(obj)
    await session.commit()


async def orm_update_user_profile_antivirus(session: AsyncSession, telegram_id: str, antivirus: int):
    obj = update(Users_profile).where(Users_profile.telegram_id == telegram_id).values(antivirus=antivirus)
    await session.execute(obj)
    await session.commit()


async def orm_update_user_profile_active_role(session: AsyncSession, telegram_id: str, active_role: int):
    obj = update(Users_profile).where(Users_profile.telegram_id == telegram_id).values(active_role=active_role)
    await session.execute(obj)
    await session.commit()


async def orm_update_user_profile_bullet(session: AsyncSession, telegram_id: str, bullet: int):
    obj = update(Users_profile).where(Users_profile.telegram_id == telegram_id).values(bullet=bullet)
    await session.execute(obj)
    await session.commit()
