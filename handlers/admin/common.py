from aiogram_dialog.widgets.kbd import SwitchTo, Cancel
from aiogram_dialog.widgets.text import Const

from handlers.admin import states_dialog as states


MAIN_MENU_BUTTON = Cancel(text=Const("🔙 Назад в Меню!"), id="__main__")
