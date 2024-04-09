from aiogram import Router
from aiogram.types import Message
from keyboards.inline.keyboard import generate_all
from lexicon import lexicon_game as lx
from filters.filters import ChatTypeFilter

router = Router()
router.message.filter(ChatTypeFilter())


start_reg_keyboard = generate_all(1, **lx.LEXICON_START_GAME)


# Этот хэндлер выводит кнопку запуска игры
@router.message()
async def delete_warning_message(message: Message):
    print(message.chat.id)
    await message.answer(message.text, reply_markup=start_reg_keyboard)