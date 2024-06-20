from sqlalchemy import select, update, delete, or_
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from config_bd.BaseModel import Plays, Plays_Go


async def add_play(
        session: AsyncSession,
        play_id: int,
        user: int,
        group: int,
        user_name: str,
        user_hero: str = '',
        is_owner: bool = False):
    """
    Добавлет в базу данных запись игрока
    :param session: AsyncSession
    :param play_id: int
    :param user: int
    :param group: int
    :param user_name: str
    :param user_hero: str
    :param is_owner: bool
    :return: None
    """
    obj = Plays(
        play_id=play_id,
        group=group,
        user=user,
        user_name=user_name,
        user_hero=user_hero,
        is_owner=is_owner
    )
    session.add(obj)
    await session.commit()


async def play_go(
        session: AsyncSession,
        play_id: int,
        is_play: bool):
    """
    Добавлет в базу данных запись игры
    :param session: AsyncSession
    :param play_id: int
    :param is_play: bool
    :return: None
    """
    obj = Plays_Go(
        play_id=play_id,
        is_play=is_play
    )
    session.add(obj)
    await session.commit()


async def select_play_user(session: AsyncSession, user: int, group: int):
    """
    Проверяет зарегистрирован ли игрок в игре группы
    :param session: AsyncSession
    :param user: int
    :param group: int
    :return: Object
    """
    stmt = select(Plays).where(
        Plays.group == group,
        Plays.user == user
    )
    result = await session.execute(stmt)
    return result.scalars().all()


async def select_play_go(session: AsyncSession):
    """
    Проверяет активацию игры
    :param session: AsyncSession
    :return: Object | None
    """
    try:
        stmt = select(Plays_Go).where(Plays_Go.is_play.is_(True))
        result = await session.execute(stmt)
        return result.scalars().one()
    except NoResultFound:
        return None


async def select_play(session: AsyncSession, play_id: int):
    """
    Получаем данные об игре
    :param session: AsyncSession
    :param play_id: int
    :return: Object
    """
    stmt = select(Plays).where(Plays.play_id == play_id)
    result = await session.execute(stmt)
    return result.scalars().one()


async def update_play_go(session: AsyncSession, play_id: int, is_play: bool):
    """
    Обновляем статус активации игры
    :param session: AsyncSession
    :param play_id: int
    :param is_play: bool
    :return: None
    """
    query = update(Plays_Go).where(Plays_Go.play_id == play_id).values(is_play=is_play)
    await session.execute(query)
    await session.commit()


async def select_play_users(session: AsyncSession, group: int):
    """
    Получаем данные о всех игроках в игре
    :param session: AsyncSession
    :param group: int
    :return: list(object)
    """
    stmt = select(Plays).where(Plays.group == group)
    result = await session.execute(stmt)
    await session.close()
    return result.scalars().all()
