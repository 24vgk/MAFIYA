import asyncio
import datetime
import time

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from yookassa import Payment

from applications import pay_yoo
from keyboards.inline import keyboard
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from lexicon import lexicon_other as lx
from config_bd.Users import orm_add_user, orm_select_user_profile, orm_add_user_profile, \
    orm_update_user_profile_on_off, orm_update_user_profile_stones, orm_update_user_profile_gold, \
    orm_update_user_profile_protection, orm_update_user_profile_antivirus, orm_update_user_profile_documents, \
    orm_update_user_profile_active_role, orm_update_user_profile_bullet, orm_select_user

# Инициализируем роутер уровня модуля
router: Router = Router()

# Этот хэндлер удаляет сообщения которые не обрабатываются
@router.message()
async def delete_warning_message(message: Message):
    print(message.chat.id)
    await message.delete()
    await message.answer(text='вы зарегистрировали игру')
