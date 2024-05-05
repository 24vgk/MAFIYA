from sqlalchemy import select, update, delete
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from config_bd.BaseModel import Users, Users_profile, Users_history_play, Users_history_balance


# РАБОТА С ТАБЛИЦЕЙ USERS

async def orm_add_user(session: AsyncSession, telegram_id: str, first_name: str, user_name: str):
    """
    Добавляет пользователя в БД
    :param session: obj
    :param telegram_id: str
    :param first_name: str
    :param user_name: str
    """
    obj = Users(
        telegram_id=telegram_id,
        first_name=first_name,
        user_name=user_name,
    )
    session.add(obj)
    await session.commit()


async def orm_select_user(session: AsyncSession, telegram_id: str):
    """
    Получаем пользователя из БД
    :param session: obj
    :param telegram_id: str
    :return: obj
    """
    query = select(Users).where(Users.telegram_id == telegram_id)
    try:
        result = await session.execute(query)
        return result.scalars().one()
    except NoResultFound:
        return None


async def orm_update_user_first_name(session: AsyncSession, telegram_id: str, first_name: str):
    obj = update(Users).where(Users.telegram_id == telegram_id).values(first_name=first_name)
    await session.execute(obj)
    await session.commit()


async def orm_update_user_user_name(session: AsyncSession, telegram_id: str, user_name: str):
    obj = update(Users).where(Users.telegram_id == telegram_id).values(user_name=user_name)
    await session.execute(obj)
    await session.commit()


async def orm_update_user_refer(session: AsyncSession, telegram_id: str, refer: str):
    obj = update(Users).where(Users.telegram_id == telegram_id).values(refer=refer)
    await session.execute(obj)
    await session.commit()


async def orm_update_user_bonus(session: AsyncSession, telegram_id: str, bonus: int):
    obj = update(Users).where(Users.telegram_id == telegram_id).values(bonus=bonus)
    await session.execute(obj)
    await session.commit()


async def orm_update_user_is_admin(session: AsyncSession, telegram_id: str, is_admin: bool):
    obj = update(Users).where(Users.telegram_id == telegram_id).values(is_admin=is_admin)
    await session.execute(obj)
    await session.commit()


async def orm_delete_user(session: AsyncSession, telegram_id: str):
    obj = delete(Users).where(Users.telegram_id == telegram_id)
    await session.execute(obj)
    await session.commit()


# РАБОТА С ТАБЛИЦЕЙ USERS_PROFILE


async def orm_add_user_profile(session: AsyncSession, telegram_id: str):
    """
    Добавляет пользователя в БД профиля
    :param session: obj
    :param telegram_id: str
    """
    obj = Users_profile(
        telegram_id=telegram_id,
    )
    session.add(obj)
    await session.commit()


async def orm_select_user_profile(session: AsyncSession, telegram_id: str):
    """
    Получаем профиль пользователя из БД
    :param session: obj
    :param telegram_id: str
    :return:
    """
    query = select(Users_profile).where(Users_profile.telegram_id == telegram_id)
    try:
        result = await session.execute(query)
        return result.scalars().one()
    except NoResultFound:
        return None


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


# РАБОТА С ТАБЛИЦЕЙ USERS_HISTORY_BALANCE

async def orm_add_user_history_balance(session: AsyncSession, telegram_id: str, type: str, comment: str, sum: int):
    """
    Добавляет данные по изменению баланса пользователя
    """
    obj = Users_history_balance(
        telegram_id=telegram_id,
        type=type,
        comment=comment,
        sum=sum
    )
    session.add(obj)
    await session.commit()


async def orm_select_user_history_balance(session: AsyncSession, telegram_id: str):
    """
    Получаем историю баланса пользователя из БД
    :param session: obj
    :param telegram_id: str
    :return: obj
    """
    query = select(Users_history_balance).where(Users_history_balance.telegram_id == telegram_id)
    try:
        result = await session.execute(query)
        return result.scalars().all()
    except NoResultFound:
        return None


async def orm_update_user_history_balance_type(session: AsyncSession, telegram_id: str, type: str):
    obj = update(Users_history_balance).where(Users_history_balance.telegram_id == telegram_id).values(type=type)
    await session.execute(obj)
    await session.commit()


async def orm_update_user_history_balance_comment(session: AsyncSession, telegram_id: str, comment: str):
    obj = update(Users_history_balance).where(Users_history_balance.telegram_id == telegram_id).values(comment=comment)
    await session.execute(obj)
    await session.commit()


async def orm_update_user_history_balance_sum(session: AsyncSession, telegram_id: str, sum: int):
    obj = update(Users_history_balance).where(Users_history_balance.telegram_id == telegram_id).values(sum=sum)
    await session.execute(obj)
    await session.commit()


# РАБОТА С ТАБЛИЦЕЙ USERS_HISTORY_PLAY

async def orm_add_user_history_play(session: AsyncSession, telegram_id: str, type: str, comment: str, num_play: int):
    """
    Добавляет данные по изменению баланса пользователя
    """
    obj = Users_history_balance(
        telegram_id=telegram_id,
        type=type,
        comment=comment,
        num_play=num_play
    )
    session.add(obj)
    await session.commit()


async def orm_select_user_history_play(session: AsyncSession, telegram_id: str):
    """
    Получаем историю игр пользователя из БД
    :param session: obj
    :param telegram_id: str
    :return: obj
    """
    query = select(Users_history_play).where(Users_history_play.telegram_id == telegram_id)
    try:
        result = await session.execute(query)
        return result.scalars().all()
    except NoResultFound:
        return None


async def orm_update_user_history_play_type(session: AsyncSession, telegram_id: str, type: str):
    obj = update(Users_history_play).where(Users_history_play.telegram_id == telegram_id).values(type=type)
    await session.execute(obj)
    await session.commit()


async def orm_update_user_history_play_comment(session: AsyncSession, telegram_id: str, comment: str):
    obj = update(Users_history_play).where(Users_history_play.telegram_id == telegram_id).values(comment=comment)
    await session.execute(obj)
    await session.commit()


async def orm_update_user_history_play_num_play(session: AsyncSession, telegram_id: str, num_play: int):
    obj = update(Users_history_play).where(Users_history_play.telegram_id == telegram_id).values(num_play=num_play)
    await session.execute(obj)
    await session.commit()
