from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter
from aiogram import types

from config_bd.Users import orm_select_user
from config_data.config import Config, load_config
from sqlalchemy.ext.asyncio import AsyncSession

config: Config = load_config()


class ChatTypeFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return '-' in str(message.chat.id)


class CallbackPrefixFilter(Filter):
    def __init__(self, prefix: str):
        self.prefix = prefix

    async def __call__(self, callback_query: types.CallbackQuery) -> bool:
        return callback_query.data.startswith(self.prefix)