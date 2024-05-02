from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram_dialog import Dialog, Window, DialogManager, StartMode
from aiogram_dialog.widgets.input import ManagedTextInput, TextInput
from aiogram_dialog.widgets.kbd import Start, SwitchTo, Cancel, Group, Button, Select
from aiogram_dialog.widgets.text import Const, Format, List, Multi

from handlers.admin import states_dialog as states
from handlers.admin.common import MAIN_MENU_BUTTON, BACK_TO_INFO_CLIENT_BUTTON
from config_bd.Users import (
    orm_add_user,
    orm_select_user_profile,
    orm_add_user_profile,
    orm_update_user_profile_on_off,
    orm_update_user_profile_stones,
    orm_update_user_profile_gold,
    orm_update_user_profile_protection,
    orm_update_user_profile_antivirus,
    orm_update_user_profile_documents,
    orm_update_user_profile_active_role,
    orm_update_user_profile_bullet,
)
from sqlalchemy.ext.asyncio import AsyncSession


# Проверка id
def check_id(id: str) -> str:
    if id.isdigit():
        return id
    raise ValueError


# Проверка на число
def check_digit(text: str) -> str:
    if text.isdigit():
        return text
    raise ValueError


# Хэндлер, который сработает, если id введён корректно
async def correct_id(
    message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str
):
    session: AsyncSession = dialog_manager.middleware_data["session"]
    user_db = await orm_select_user_profile(session, text)
    # если пользователь есть в базе переводи в след сосотояние
    if user_db is not None:
        dialog_manager.dialog_data.update({"tg_id": text})
        await dialog_manager.switch_to(states.WorkingClients.CORRECT_ID)
    # если пользоваетля нет в базе, просим ввести id повторно
    else:
        await message.answer(text="id не найден, повторите ввод")
        dialog_manager.dialog_data.clear()
        await dialog_manager.switch_to(states.WorkingClients.MAIN)


# Хэндлер, который сработает, если введён не id
async def uncorrect_id(
    message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str
):
    await message.answer(text="id неккоректен, повторите ввод")
    dialog_manager.dialog_data.clear()
    await dialog_manager.switch_to(states.WorkingClients.MAIN)


# Хэндлер запиывает нажатую кнопку для передачи в хэндлер обработки текста
async def select_currency(
    button: Button, callback: CallbackQuery, dialog_manager: DialogManager, item_id: str
):
    dialog_manager.dialog_data.update({"currency": item_id})
    await dialog_manager.switch_to(states.WorkingClients.INPUT_NEW_VALUE)


# Хэндлер, который сработает после ввода нового значения ДОПИСАТЬ ЗАПИСЬ В ИСТОРИЮ ТРАНЗАКЦИЙ!!!!!!
async def correct_new_balance(
    message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str
):
    tg_id = dialog_manager.dialog_data["tg_id"]
    currency = dialog_manager.dialog_data["currency"]
    session = dialog_manager.middleware_data["session"]
    new_value = int(text)
    dialog_manager.dialog_data.update({"amount": new_value})
    if currency == "gold":
        await orm_update_user_profile_gold(session, tg_id, new_value)
    elif currency == "stones":
        await orm_update_user_profile_stones(session, tg_id, new_value)
    elif currency == "protection":
        await orm_update_user_profile_protection(session, tg_id, new_value)
    elif currency == "documents":
        await orm_update_user_profile_documents(session, tg_id, new_value)
    elif currency == "antivirus":
        await orm_update_user_profile_antivirus(session, tg_id, new_value)
    elif currency == "active_role":
        await orm_update_user_profile_active_role(session, tg_id, new_value)
    elif currency == "bullet":
        await orm_update_user_profile_bullet(session, tg_id, new_value)
    await dialog_manager.switch_to(states.WorkingClients.SEND_UPDATE_VALUE)


# Хэндлер, который сработает, если введено не число при вводе не числа
async def uncorrect_new_balance(
    message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str
):
    await message.answer("Введено не число. Повторите ввод.")
    await dialog_manager.switch_to(states.WorkingClients.INPUT_NEW_VALUE)


# Хэндлер который отправит сообщение юзеру при изменении баланса
async def send_balance_user(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    tg_id = dialog_manager.dialog_data["tg_id"]
    amount = dialog_manager.dialog_data["amount"]
    output_currency = dialog_manager.dialog_data["output_currency"]
    # высылаем сообщение пользователю
    await callback.bot.send_message(
        chat_id=tg_id,
        text="Ваш баланс внутриигровой валюты {output_currency} изменен технической поддержкой ✅\n\n"
        f"Текущий баланс {output_currency}: {amount}",
        # reply_markup=inline.distribution_admin, КНОПКА В ЛИЧНЫЙ КАБИНЕТ
    )
    await dialog_manager.switch_to(states.WorkingClients.CORRECT_ID)


# Хэндлер который сработает при нажатии Удалить в Удалить клиента
async def deleting_user(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    tg_id = dialog_manager.dialog_data["tg_id"]
    session: AsyncSession = dialog_manager.middleware_data["session"]
    # Удаляем клиента в базе
    print("УДАЛЕНИЕ")
    await dialog_manager.switch_to(state=states.WorkingClients.DELETING)


# Геттер для передачи данных о пользователе в окно
async def id_getter(dialog_manager: DialogManager, **kwargs):
    tg_id = dialog_manager.dialog_data["tg_id"]
    session: AsyncSession = dialog_manager.middleware_data["session"]
    user_db = await orm_select_user_profile(session, tg_id)
    return {
        # добавить имя и юзернейм
        "tg_id": tg_id,
        "gold": user_db.gold,
        "stones": user_db.stones,
        "protection": user_db.protection,
        "documents": user_db.documents,
        "antivirus": user_db.antivirus,
        "active_role": user_db.active_role,
        "bullet": user_db.bullet,
    }


# Геттер для передачи валют в окно
async def get_currency(**kwargs):
    currency = [
        ("💰 Золото", "gold"),
        ("💎 Камни", "stones"),
        ("🛡 Защита", "protection"),
        ("📂 Документы", "documents"),
        ("📀 Антивирус", "antivirus"),
        ("🎎 Активная роль", "active_role"),
        ("☠ Бронебойная пуля", "bullet"),
    ]
    return {"currency": currency}


# Геттер передачи выбранно валюты
async def select_currency_getter(dialog_manager: DialogManager, **kwargs):
    currency = dialog_manager.dialog_data["currency"]
    if currency == "gold":
        output_currency = "💰 Золото"
    elif currency == "stones":
        output_currency = "💎 Камни"
    elif currency == "protection":
        output_currency = "🛡 Защита"
    elif currency == "documents":
        output_currency = "📂 Документы"
    elif currency == "antivirus":
        output_currency = "📀 Антивирус"
    elif currency == "active_role":
        output_currency = "🎎 Активная роль"
    elif currency == "bullet":
        output_currency = "☠ Бронебойная пуля"
    dialog_manager.dialog_data.update({"output_currency": output_currency})
    return {"output_currency": output_currency}


# Геттер передачи в окно сообщения о изменении баланса
async def send_update_value_getter(dialog_manager: DialogManager, **kwargs):
    return dialog_manager.dialog_data


# Геттер для передачи данных о пользователе в окно удаления
async def id_for_del_getter(dialog_manager: DialogManager, **kwargs):
    tg_id = dialog_manager.dialog_data["tg_id"]
    return {"tg_id": tg_id}


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


# Окно работы с клиентом
correct_id_window = Window(
    Multi(
        # Format("<b>User:</b> {name_user}\n", when="name_user"),
        Format("<b>ID:</b> <code>{tg_id}</code>"),
        # Format("\n<b>Username:</b> <code>{login}</code>", when="login"),
        Format(
            "💰 Золото: {gold}\n"
            "💎 Камни: {stones}\n"
            "🛡 Защита: {protection}\n"
            "📂 Документы: {documents}\n"
            "📀 Антивирус: {antivirus}\n"
            "🎎 Активная роль: {active_role}\n"
            "☠ Бронебойная пуля: {bullet}\n"
        ),
    ),
    Group(
        SwitchTo(
            text=Const("Изменить баланс"),
            id="update_balance",
            state=states.WorkingClients.NEW_BALANCE,
        ),
        SwitchTo(
            text=Const("История"),
            id="history_pay",
            state=states.WorkingClients.HISTORY,
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


# Окно изменить баланс
new_balance_window = Window(
    Const("Выберите внутриигровую валюту которую вы хотите изменить"),
    Group(
        Select(
            Format("{item[0]}"),
            id="currency",
            item_id_getter=lambda x: x[1],
            items="currency",
            on_click=select_currency,
        ),
        width=2,
    ),
    BACK_TO_INFO_CLIENT_BUTTON,
    getter=get_currency,
    state=states.WorkingClients.NEW_BALANCE,
)


# Окно ввода нового значения
input_new_value_window = Window(
    Format(text="Введите новое значение внутриигровой валюты {output_currency}:"),
    TextInput(
        id="new_value_input",
        type_factory=check_digit,
        on_success=correct_new_balance,
        on_error=uncorrect_new_balance,
    ),
    getter=select_currency_getter,
    state=states.WorkingClients.INPUT_NEW_VALUE,
)


# Окно вывода сообщения о изменении баланса
send_update_value_window = Window(
    Format(
        text="Баланс внутриигровой валюты {output_currency} для клиента с id {tg_id} изменен на {amount}\n\n"
        "Выслать уведомление клиенту?"
    ),
    Group(
        SwitchTo(
            text=Const("Нет"), id="no_send_balance_user", state=states.WorkingClients.CORRECT_ID
        ),
        Button(text=Const("Да"), id="send_balance_user", on_click=send_balance_user),
    ),
    getter=send_update_value_getter,
    state=states.WorkingClients.SEND_UPDATE_VALUE,
)


# Окно Удалить клиента
delete_user_window = Window(
    Format(text="Уверены что хотите удалить клиента -  {tg_id} ?"),
    Group(
        SwitchTo(
            text=Const("Нет"), id="no_deleting", state=states.WorkingClients.CORRECT_ID
        ),
        Button(text=Const("Удалить"), id="deleting_user", on_click=deleting_user),
    ),
    getter=id_for_del_getter,
    state=states.WorkingClients.DELETE_USER,
)


# Окно вывода сообщения о удалении клиента
deleting_user_window = Window(
    Format(text=" Клиент - {tg_id} удален 🗑️"),
    MAIN_MENU_BUTTON,
    getter=id_for_del_getter,
    state=states.WorkingClients.DELETING,
)

working_clients_dialog = Dialog(
    working_clients_window,
    correct_id_window,
    new_balance_window,
    input_new_value_window,
    send_update_value_window,
    delete_user_window,
    deleting_user_window,
)
