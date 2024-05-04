import logging
import os

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram_dialog import Dialog, Window, DialogManager, StartMode
from aiogram_dialog.widgets.input import ManagedTextInput, TextInput
from aiogram_dialog.widgets.kbd import Start, SwitchTo, Cancel, Group, Button, Select
from aiogram_dialog.widgets.text import Const, Format, List, Multi
from sqlalchemy.ext.asyncio import AsyncSession

from handlers.admin import states_dialog as states
from handlers.admin.common import MAIN_MENU_BUTTON, BACK_TO_INFO_CLIENT_BUTTON
from config_bd.Users import (
    orm_add_user,
    orm_select_user,
    orm_update_user_first_name,
    orm_update_user_user_name,
    orm_update_user_refer,
    orm_update_user_bonus,
    orm_update_user_is_admin,
    orm_delete_user,
    orm_add_user_profile,
    orm_select_user_profile,
    orm_update_user_profile_on_off,
    orm_update_user_profile_stones,
    orm_update_user_profile_gold,
    orm_update_user_profile_protection,
    orm_update_user_profile_antivirus,
    orm_update_user_profile_documents,
    orm_update_user_profile_active_role,
    orm_update_user_profile_bullet,
    orm_select_user_history_balance,
    orm_update_user_history_balance_type,
    orm_update_user_history_balance_comment,
    orm_update_user_history_balance_sum,
    orm_select_user_history_play,
    orm_update_user_history_play_type,
    orm_update_user_history_play_comment,
    orm_update_user_history_play_num_play,
)

services_scripts_window = Window(
    Const("В данном разделе ведутся творческо-технические работы. Вернитесь позже."),
    MAIN_MENU_BUTTON,
    state=states.ServiceScripts.MAIN,
)


services_scripts_dialog = Dialog(services_scripts_window)
