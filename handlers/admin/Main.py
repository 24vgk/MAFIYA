from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram_dialog import Dialog, Window, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Start, SwitchTo, Cancel, Group
from aiogram_dialog.widgets.text import Const

from handlers.admin import states_dialog as states
from handlers.admin.common import MAIN_MENU_BUTTON


main_menu_dialog = Dialog(
    Window(
        Const("Меню Владельца"),
        Group(
            Start(
                Const("Работа с клиентами"),
                id="working_clients",
                state=states.WorkingClients.MAIN,
            ),
            Start(
                Const("Рассылки"), id="send_messages", state=states.SendMessages.MAIN
            ),
            Start(
                Const("Сервисные скрипты"),
                id="service_scripts",
                state=states.ServiceScripts.MAIN,
            ),
            width=2,
        ),
        state=states.Main_menu.MAIN,
    )
)
