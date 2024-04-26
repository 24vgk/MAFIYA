from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram_dialog import Dialog, Window, DialogManager, StartMode
from aiogram_dialog.widgets.input import ManagedTextInput, TextInput
from aiogram_dialog.widgets.kbd import Start, SwitchTo, Cancel, Group
from aiogram_dialog.widgets.text import Const, Format, List, Multi

from handlers.admin import states_dialog as states
from handlers.admin.common import MAIN_MENU_BUTTON


# Проверка id на наличие в базе пользователей
def check_id(id: str) -> str:
    # s = SQL()
    # if s.SELECT_USER(id) is not None:
    if id in ["474528766", "725455605"]:
        return id
    raise ValueError


# Хэндлер, который сработает, если пользователь присутствует в базе пользователей
async def correct_id(
    message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str
):
    dialog_manager.dialog_data.update({"tg_id": text})
    await dialog_manager.switch_to(states.WorkingClients.CORRECT_ID)


# Хэндлер, который сработает, если пользователь отсутствует в базе пользователей
async def uncorrect_id(
    message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str
):
    await message.answer(text="id не найден, повторите ввод")
    dialog_manager.dialog_data.clear()
    await dialog_manager.switch_to(states.WorkingClients.MAIN)


# Геттер для передачи данных о пользователе в окно
async def id_getter(dialog_manager: DialogManager, **kwargs):
    tg_id = dialog_manager.dialog_data["tg_id"]
    return {
        "tg_id": tg_id,
    }


# Окно ввода id клиента
working_clients_window = Window(
    Const(text="Введите tg id клиента:"),
    TextInput(
        id="id_input",
        type_factory=check_id,
        on_success=correct_id,
        on_error=uncorrect_id,
    ),
    MAIN_MENU_BUTTON,
    state=states.WorkingClients.MAIN,
)


correct_id_window = Window(
    Multi(
        # Format("<b>User:</b> {name_user}\n", when="name_user"),
        Format("<b>ID:</b> <code>{tg_id}</code>"),
        # Format("\n<b>Username:</b> <code>{login}</code>", when="login"),
        # Format("\n\n<b>Баланс:</b> {balance} 💵\n\n"),
    ),
    Group(
        SwitchTo(
            text=Const("Изменить баланс"),
            id="update_balance",
            state=states.WorkingClients.INPUT_NEW_BALANCE,
        ),
        SwitchTo(
            text=Const("История платежей"),
            id="history_pay",
            state=states.WorkingClients.HISTORY_PAY,
        ),
        SwitchTo(
            text=Const("Начислить бонусы"),
            id="add_bonus",
            state=states.WorkingClients.INPUT_BONUS,
        ),
        SwitchTo(
            text=Const("Удалить клиента"),
            id="delete_user",
            state=states.WorkingClients.DELETE_USER,
        ),
        MAIN_MENU_BUTTON,
        width=2,
    ),
    getter=id_getter,
    state=states.WorkingClients.CORRECT_ID,
)


working_clients_dialog = Dialog(working_clients_window, correct_id_window)