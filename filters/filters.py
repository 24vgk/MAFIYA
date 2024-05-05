from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

from config_bd.Users import orm_select_user
from config_data.config import Config, load_config
from sqlalchemy.ext.asyncio import AsyncSession

config: Config = load_config()


class ChatTypeFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return '-' in str(message.chat.id)
