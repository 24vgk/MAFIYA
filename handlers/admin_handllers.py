from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import StartMode
from aiogram_dialog import DialogManager

from handlers.admin import states_dialog as states
from filters.filters import IsOwner

router: Router = Router()
router.message.filter(IsOwner())


# Админка
@router.message(F.text == "Владелец")
async def admin_menu(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=states.Main.MAIN, mode=StartMode.RESET_STACK)
