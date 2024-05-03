from aiogram_dialog.widgets.kbd import SwitchTo, Cancel
from aiogram_dialog.widgets.text import Const

from handlers.admin import states_dialog as states


MAIN_MENU_BUTTON = Cancel(text=Const("🔙 Назад в Меню!"), id="__main__")


BACK_TO_INFO_CLIENT_BUTTON = SwitchTo(
    text=Const("🔙 Назад"),
    id="back_to_info_client",
    state=states.WorkingClients.CORRECT_ID,
)