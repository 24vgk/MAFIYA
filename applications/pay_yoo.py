import uuid
from yookassa import Configuration, Payment
from config_data.config import Config, load_config

config: Config = load_config()

Configuration.account_id = config.tg_bot.yoo_id
Configuration.secret_key = config.tg_bot.yoo_token


def pay(val: str, des: str):
    dict_x = {}
    payment = Payment.create({
        "amount": {
            "value": val,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://t.me/mafiya_zov_bot"
        },
        "capture": True,
        "receipt": {
            "customer": {
                "phone": "79939133738"
            },
            "items": [
                {
                    "description": des,
                    "quantity": "1.00",
                    "amount": {
                        "value": val,
                        "currency": "RUB"
                    },
                    "vat_code": "2",
                    "payment_mode": "full_prepayment",
                    "payment_subject": "commodity"
                },
            ]
        },
    }, uuid.uuid4())
    dict_x['status'] = payment.status
    dict_x['url'] = payment.confirmation.confirmation_url
    dict_x['id'] = payment.id
    return dict_x


def pay_auto(val: str, des: str):
    dict_x = {}
    payment = Payment.create({
        "amount": {
            "value": val,
            "currency": "RUB"
        },
        "payment_method_data": {
            "type": "bank_card"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "Адрес возврата"
        },
        "capture": True,
        "description": des,
        "save_payment_method": True
    }, uuid.uuid4())
    dict_x['status'] = payment.status
    dict_x['url'] = payment.confirmation.confirmation_url
    dict_x['id'] = payment.id
    return dict_x