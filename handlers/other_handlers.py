from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from keyboards.inline import keyboard
from lexicon import lexicon_other as lx
# Инициализируем роутер уровня модуля
router: Router = Router()


start_keyboard = keyboard.generate_all(2, **lx.LEXICON_START)


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        text=lx.LEXICON_START_TEXT['start_text'].format(
            user_name=message.from_user.first_name
        ), reply_markup=start_keyboard
    )


@router.message(Command(commands='my_id'))
async def com_help(message: Message):
    await message.answer(text=str(message.from_user.id))


# # Этот хэндлер удаляет сообщения которые не обрабатываются
# @router.message()
# async def delete_warning_message(message: Message):
#     print(message.text)
#     await message.delete()