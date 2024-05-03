from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from keyboards.inline.keyboard import generate_all
from lexicon import lexicon_game as lx
from filters.filters import ChatTypeFilter
from config_bd import Plays as pl

router = Router()
router.message.filter(ChatTypeFilter())


start_reg_keyboard = generate_all(1, **lx.LEXICON_START_GAME)


# Этот хэндлер выводит кнопку запуска игры
@router.message()
async def delete_warning_message(message: Message):
    print(message.chat.id)
    await message.answer(message.text, reply_markup=start_reg_keyboard)


@router.callback_query(F.data == 'start_reg')
async def com_help(callback: CallbackQuery, session: AsyncSession):
    print(callback)
    if callback.message.chat.id == -1001892980253:
        if pl.select_play_user(session, callback.from_user.id, callback.message.chat.id) is not None:
            await callback.message.answer(text='Вы уже играете')
        else:
        # await callback.message.delete()
            await pl.add_play(session, callback.from_user.id, callback.message.chat.id)
            await callback.message.answer(lx.LEXICON_GAME_START['start_game'])
            await callback.message.bot.send_message(callback.from_user.id, lx.LEXICON_GAME_START['start_game'])