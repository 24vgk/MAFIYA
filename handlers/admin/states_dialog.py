from aiogram.fsm.state import State, StatesGroup


class Main_menu(StatesGroup):
    MAIN = State()


class WorkingClients(StatesGroup):
    MAIN = State()
    CORRECT_ID = State()
    INPUT_NEW_BALANCE = State()
    HISTORY_PAY = State()
    INPUT_BONUS = State()
    DELETE_USER = State()


class SendMessages(StatesGroup):
    MAIN = State()


class ServiceScripts(StatesGroup):
    MAIN = State()


class GetLogs(StatesGroup):
    MAIN = State()
