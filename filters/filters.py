from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from config_data.config import Config, load_config

config: Config = load_config()


class IsOwner(BaseFilter):

    async def __call__(self, message: Message) -> bool:
        admin_ids = config.tg_bot.admin_ids
        return message.from_user.id in admin_ids


class ChatTypeFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return '-' in str(message.chat.id)
