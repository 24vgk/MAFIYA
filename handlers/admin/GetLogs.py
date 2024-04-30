from aiogram import Router, F
from aiogram.types import FSInputFile
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram_dialog import Dialog, Window, DialogManager, StartMode
from aiogram_dialog.widgets.input import ManagedTextInput, TextInput
from aiogram_dialog.widgets.kbd import Start, SwitchTo, Cancel, Group, Button
from aiogram_dialog.widgets.text import Const, Format, List, Multi

from handlers.admin import states_dialog as states
from handlers.admin.common import MAIN_MENU_BUTTON






async def error(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    if callback.from_user.id == 474528766 or callback.from_user.id == 725455605:
        file_name = f"ERROR.txt"
        document = FSInputFile(file_name)
        await callback.message.answer_document(document)
    else:
        await callback.answer('Доступ запрещён')



get_logs_window = Window(Const("Выберите типы ошибок которые нужно вывести"),
                         Button(Const("Получить ошибки"), id="get_error", on_click=error),
                         MAIN_MENU_BUTTON,
                         state=states.GetLogs.MAIN)

get_logs_dialog = Dialog(get_logs_window)