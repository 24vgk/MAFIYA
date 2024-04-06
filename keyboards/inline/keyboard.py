from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon import lexicon_other


# Функция генератор универсальный
def generate_all(width: int, *args: str, **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализация билдера
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Инициализация списка кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполнение списка кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(text=text, callback_data=button))

    kb_builder.row(*buttons, width=width)
    return kb_builder.as_markup()
