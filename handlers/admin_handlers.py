from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram_dialog import Dialog, Window, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Start, SwitchTo, Cancel
from aiogram_dialog.widgets.text import Const

from keyboards.inline import keyboard
from handlers.admin import states_dialog as states
from handlers.admin.common import MAIN_MENU_BUTTON


router: Router = Router()


# Админка
@router.callback_query(F.data == 'adm')
async def admin_menu(callback: CallbackQuery, dialog_manager: DialogManager):
    await dialog_manager.start(state=states.Main_menu.MAIN, mode=StartMode.RESET_STACK)
