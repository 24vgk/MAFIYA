LEXICON_CONTACTS: dict[str, str] = {
    "faq": "https://t.me/e_zov_teh",  # добавить ссылку на FAQ сайта
    "support": "https://t.me/e_zov_teh",  # добавить ссылку на тех. поддержку
    "referal_link": "https://t.me/mafiya_zov_bot?start={id}",
}


LEXICON_START: dict[str, str] = {
    "script": "Сценарий",
    "profile": "Профиль",
    "info": "Информация"
}

LEXICON_START_TEXT: dict[str, str] = {
    "start_text": "Приветствую тебя {user_name}!\n\n"
                  "Я готов провести незабываемую игру для тебя и твоей компании!\n\n"
                  "Осмотрись, я приготовил для вас много интересных сценариев..."
}

LEXICON_PROFILE: dict[str: str] = {
    "info_user": "💰 Золото: {gold}\n"
                 "💎 Камни: {stones}\n"
                 "🛡 Защита: {protection}\n"
                 "📂 Документы: {documents}\n"
                 "📀 Антивирус: {antivirus}\n"
                 "🎎 Активная роль: {active_role}\n"
                 "☠ Бронебойная пуля: {bullet}\n\n"
                 "⚠ Настройка использования предметов не применяется во время игры! "
                 "Предметы купленные во время игры не работают!"
}

LEXICON_PROFILE_BUTTON_ON: dict[str: str] = {
    "shop": "🔮 Магическая лавка",
    "on": "Предметы в игре ✅",
    "back_profile": "Назад"
}

LEXICON_PROFILE_BUTTON_OFF: dict[str: str] = {
    "shop": "🔮 Магическая лавка",
    "off": "Предметы в игре ❌",
    "back_profile": "Назад"
}

LEXICON_SHOP: dict[str: str] = {
    "shop_text": "Что будем покупать?\n\n"
                 "🛡 Защита ({protection} шт.)\n"
                 "Один раз может спасти тебе жизнь\n\n"
                 "📂 Документы ({documents} шт.)\n"
                 "Фальшивые документы могут пригодиться когда твою роль кто-то захочет проверить\n\n"
                 "📀 Антивирус ({antivirus} шт.)\n"
                 "Спасает твой ПК от хакера\n\n"
                 "🎎 Активная роль ({active_role} шт.)\n"
                 "Даёт 99% шанс выпадения активной роли\n\n"
                 "☠ Бронебойная пуля ({bullet} шт.)\n"
                 "Сносит все на своем пути, жертву не спасет доктор или защита, "
                 "у счастливчика нет шансов выжить, спасет только телохранитель\n\n"
                 "Ваш баланс: {gold} 💰 и {stones} 💎"
}

LEXICON_SHOP_BUTTON: dict[str: str] = {
    "shop_protection": "🛡 Защита (100 💰)",
    "shop_documents": "📂 Документы (150 💰)",
    "shop_antivirus": "📀 Антивирус (150 💰)",
    "shop_active_role": "🎎 Активная роль (1 💎)",
    "shop_bullet": "☠ Бронебойная пуля (1 💎)",
    "shop_gold": "💰100 Золота (1 💎)",
    "shop_1_stones": "💎 1 бриллиант (40 руб.)",
    "shop_2_stones": "💎 2 бриллианта (80 руб.)",
    "shop_5_stones": "💎 5 бриллиантов (180 руб.)",
    "shop_10_stones": "💎 10 бриллиантов (300 руб.)",
    "back_shop": "Назад"
}

LEXICON_SHOP_SUM: dict[str: int] = {
    "1": 40,
    "2": 80,
    "5": 180,
    "10": 300
}

LEXICON_PROFILE_BUTTON_PAY: dict[str: str] = {
    "pay": "💸 Оплатить",
    "back_profile": "Назад"
}
