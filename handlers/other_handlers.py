from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from keyboards.inline import keyboard
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from lexicon import lexicon_other as lx
from config_bd.Users import orm_add_user, orm_select_user_profile, orm_add_user_profile

# Инициализируем роутер уровня модуля
router: Router = Router()

start_keyboard = keyboard.generate_all(2, **lx.LEXICON_START)


# Стартовый
@router.message(CommandStart())
async def start(message: Message, session: AsyncSession):
    try:
        await orm_add_user(
            session,
            str(message.from_user.id),
            message.from_user.first_name,
            message.from_user.username
        )
        await orm_add_user_profile(session, str(message.from_user.id))
        await message.answer(
            text=lx.LEXICON_START_TEXT['start_text'].format(
                user_name=message.from_user.first_name
            ), reply_markup=start_keyboard
        )
    except IntegrityError:
        await message.answer(
            f'С возвращением {message.from_user.first_name}',
            reply_markup=start_keyboard
        )


@router.callback_query(F.data == "profile")
async def profile(callback: CallbackQuery, session: AsyncSession):
    obj = await orm_select_user_profile(session, str(callback.from_user.id))
    await callback.message.edit_text(
        lx.LEXICON_PROFILE["info_user"].format(
            gold=obj.gold,
            stones=obj.stones,
            protection=obj.protection,
            documents=obj.documents,
            antivirus=obj.antivirus,
            active_role=obj.active_role,
            bullet=obj.bullet
        ), reply_markup=start_keyboard
    )


@router.message(Command(commands='my_id'))
async def com_help(message: Message):
    await message.answer(text=str(message.from_user.id))

# Этот хэндлер удаляет сообщения которые не обрабатываются
@router.message()
async def delete_warning_message(message: Message):
    print(message.text)
    await message.delete()
