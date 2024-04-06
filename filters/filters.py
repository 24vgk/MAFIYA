from typing import Any
from aiogram.filters import Command, CommandStart, BaseFilter
from aiogram.types import Message, CallbackQuery
from config_data.config import Config, load_config
from config_bd.Users import SQL

config: Config = load_config()


class IsOwner(BaseFilter):

    async def __call__(self, message: Message) -> bool:
        admin_ids = config.tg_bot.admin_ids
        return message.from_user.id in admin_ids
