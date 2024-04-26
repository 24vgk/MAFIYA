from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram_dialog import Dialog, Window, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Start, SwitchTo, Cancel
from aiogram_dialog.widgets.text import Const

from keyboards.inline import keyboard
from handlers.admin import states_dialog as states
from handlers.admin.common import MAIN_MENU_BUTTON
from filters.filters import IsOwner


router: Router = Router()
router.message.filter(IsOwner())


# Админка
@router.message(Command(commands='admin'))
async def admin_menu(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=states.Main_menu.MAIN, mode=StartMode.RESET_STACK)
