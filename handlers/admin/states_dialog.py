from aiogram.fsm.state import State, StatesGroup


class Main_menu(StatesGroup):
    MAIN = State()


# Классы состояний меню работа с клиентом
class WorkingClients(StatesGroup):
    MAIN = State()
    CORRECT_ID = State()
    # Изменение баланса
    BALANCE = State()
    INPUT_NEW_BALANCE = State()
    CONFIRM_NEW_BALANCE = State()
    SEND_UPDATE_BALANCE = State()
    # Начислить бонус
    BONUS = State()
    INPUT_BONUS = State()
    CONFIRM_ADD_BONUS = State()
    # Истории
    HISTORY = State()
    HISTORY_PAY = State()
    ALL_HISTORY_PAY = State()
    HISTORY_PLAYS = State()
    ALL_HISTORY_PLAYS = State()
    # Удалить клиента
    DELETE_USER = State()
    DELETING = State()


class SendMessages(StatesGroup):
    MAIN = State()


class ServiceScripts(StatesGroup):
    MAIN = State()


class GetLogs(StatesGroup):
    MAIN = State()
