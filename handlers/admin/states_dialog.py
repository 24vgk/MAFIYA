from aiogram.fsm.state import State, StatesGroup


class Main_menu(StatesGroup):
    MAIN = State()


# Классы состояний меню работа с клиентом
class WorkingClients(StatesGroup):
    MAIN = State()
    CORRECT_ID = State()
    # Изменение баланса
    NEW_BALANCE = State()
    INPUT_NEW_VALUE = State()
    SEND_UPDATE_VALUE = State()
    HISTORY = State()
    INPUT_BONUS = State()
    # Удалить клиента
    DELETE_USER = State()
    DELETING = State()


class SendMessages(StatesGroup):
    MAIN = State()


class ServiceScripts(StatesGroup):
    MAIN = State()


class GetLogs(StatesGroup):
    MAIN = State()
