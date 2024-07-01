import asyncio
import time
import random

import apscheduler
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from handlers import sheduler_distribution
from keyboards.inline.keyboard import generate_all
from lexicon import lexicon_game as lx
from filters.filters import ChatTypeFilter, CallbackPrefixFilter
from config_bd import Plays as pl
from config_bd import Users as us
from middlewares.apscheduler_m import SchedulerMiddleware

router = Router()
router.message.filter(ChatTypeFilter())
# router.message.middleware(SchedulerMiddleware)


start_reg_keyboard = generate_all(1, **lx.LEXICON_START_GAME)
connect_reg_keyboard = generate_all(1, **lx.LEXICON_GAME_CONNECT)


# Этот хэндлер выводит кнопку запуска игры
@router.message(F.text == 'start')
async def delete_warning_message(message: Message):
    print(message.chat.id)
    await message.answer(message.text, reply_markup=start_reg_keyboard)


# Этот хэндлер отвечает за присоединение к игре
@router.callback_query(CallbackPrefixFilter(prefix='connect_game_'))
async def com_help(callback: CallbackQuery, session: AsyncSession):
    if callback.message.chat.id == -1001892980253:
        play_id = callback.data.split('_')[2]
        u = await pl.select_play_user(session, callback.from_user.id, callback.message.chat.id)
        if len(u) != 0:
            await callback.message.answer(text='Вы уже играете')
        else:
            user = await us.orm_select_user(session, str(callback.from_user.id))
            await pl.add_play(
                session,
                play_id=play_id,
                user=callback.from_user.id,
                group=callback.message.chat.id,
                user_name=user.user_name,
                is_owner=False
            )
            await callback.message.bot.send_message(callback.from_user.id, lx.LEXICON_GAME_START['start_game'])


# Этот хэндлер отвечает за регистрацию игры
@router.callback_query(F.data == 'start_reg')
async def com_help(callback: CallbackQuery, session: AsyncSession):
    if callback.message.chat.id == -1001892980253:
        x = await pl.select_play_user(session, callback.from_user.id, callback.message.chat.id)
        if len(x) != 0:
            await callback.message.answer(text='Вы уже играете')
        else:
            user = await us.orm_select_user(session, str(callback.from_user.id))
            play_id = random.randint(1, 999999)
            await pl.add_play(
                session,
                play_id=play_id,
                user=callback.from_user.id,
                group=callback.message.chat.id,
                user_name=user.user_name,
                is_owner=True
            )
            # активируем игру
            await pl.play_go(session, play_id, True, False)
            await callback.message.bot.send_message(callback.from_user.id, lx.LEXICON_GAME_START['start_game'])
