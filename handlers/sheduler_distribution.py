import asyncio

from aiogram import Bot
from sqlalchemy.ext.asyncio import AsyncSession
from config_bd import Plays as pl

from config_data.config import load_config, Config
from keyboards.inline import generate_all
from lexicon import lexicon_game as lx

# Импортируем конфиг
config: Config = load_config()


async def reg_game(bot: Bot, session: AsyncSession):
    # Проверяем наличие активированных игр
    active_game = await pl.select_play_active(session)
    # Таймаут регистрации игры
    time = 120
    if active_game:
        # Изменяем статус игры чтобы не взял в работу снова
        await pl.update_play_active(session, active_game.play_id, False)
        # Получаем данные об игре
        play_x = await pl.select_play(session, active_game.play_id)
        chat_id = play_x.group
        flag = 0
        message_id = 0
        # Импортируем клавиатуры
        lexicon_key = {f"connect_game_{active_game.play_id}": "Присоединиться к игре"}
        connect_reg_keyboard = generate_all(1, **lexicon_key)
        while time:
            text = f"До окончания регистрации осталось {time} секунд\n\nУчастники:\n"
            # Получаем список зарегистрированных игроков
            users = await pl.select_play_users(session, chat_id)
            for u in users:
                text += f'{u.user_name}\n'
            if flag == 0:
                message_id = await bot.send_message(chat_id, text=text, reply_markup=connect_reg_keyboard)
                flag = 1
            else:
                await bot.edit_message_text(chat_id=chat_id, message_id=message_id.message_id, text=text, reply_markup=connect_reg_keyboard)
            time -= 10
            await asyncio.sleep(10)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id.message_id, text='Время регистрации закончилось')
        count_user = len(await pl.select_play_users(session, chat_id))
        if count_user < 4:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id.message_id, text='Недостаточно игроков для игры')
        else:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id.message_id, text='Игра начинается')
            await pl.update_play_go(session, active_game.play_id, True)


async def active_game(bot: Bot, session: AsyncSession):
    # Проверяем наличие активированных игр
    play_go = await pl.select_play_go(session)
