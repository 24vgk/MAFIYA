import asyncio
import datetime
import time

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from yookassa import Payment

from applications import pay_yoo
from keyboards.inline import keyboard
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from lexicon import lexicon_other as lx
from config_bd.Users import orm_add_user, orm_select_user_profile, orm_add_user_profile, \
    orm_update_user_profile_on_off, orm_update_user_profile_stones, orm_update_user_profile_gold, \
    orm_update_user_profile_protection, orm_update_user_profile_antivirus, orm_update_user_profile_documents, \
    orm_update_user_profile_active_role, orm_update_user_profile_bullet

# Инициализируем роутер уровня модуля
router: Router = Router()

start_keyboard = keyboard.generate_all(2, **lx.LEXICON_START)
profile_keyboard_on = keyboard.generate_all(1, **lx.LEXICON_PROFILE_BUTTON_ON)
profile_keyboard_off = keyboard.generate_all(1, **lx.LEXICON_PROFILE_BUTTON_OFF)
shop_keyboard = keyboard.generate_all(2, **lx.LEXICON_SHOP_BUTTON)


# Стартовый
@router.message(CommandStart())
async def start(message: Message, session: AsyncSession):
    try:
        await orm_add_user(
            session,
            str(message.from_user.id),
            message.from_user.first_name,
            message.from_user.username
        )
        await orm_add_user_profile(session, str(message.from_user.id))
        await message.answer(
            text=lx.LEXICON_START_TEXT['start_text'].format(
                user_name=message.from_user.first_name
            ), reply_markup=start_keyboard
        )
    except IntegrityError:
        await message.answer(
            f'С возвращением {message.from_user.first_name}',
            reply_markup=start_keyboard
        )


@router.callback_query(F.data == "back_profile")
async def back_start(callback: CallbackQuery):
    await callback.message.edit_text(
        text=lx.LEXICON_START_TEXT['start_text'].format(
            user_name=callback.message.from_user.first_name
        ), reply_markup=start_keyboard
    )


@router.callback_query(F.data == "back_shop")
@router.callback_query(F.data == "profile")
async def profile(callback: CallbackQuery, session: AsyncSession):
    obj = await orm_select_user_profile(session, str(callback.from_user.id))
    if obj.on_off:
        await callback.message.edit_text(
            lx.LEXICON_PROFILE["info_user"].format(
                gold=obj.gold,
                stones=obj.stones,
                protection=obj.protection,
                documents=obj.documents,
                antivirus=obj.antivirus,
                active_role=obj.active_role,
                bullet=obj.bullet
            ), reply_markup=profile_keyboard_on
        )
    else:
        await callback.message.edit_text(
            lx.LEXICON_PROFILE["info_user"].format(
                gold=obj.gold,
                stones=obj.stones,
                protection=obj.protection,
                documents=obj.documents,
                antivirus=obj.antivirus,
                active_role=obj.active_role,
                bullet=obj.bullet
            ), reply_markup=profile_keyboard_off
        )


@router.callback_query(F.data == "shop")
async def profile(callback: CallbackQuery, session: AsyncSession):
    obj = await orm_select_user_profile(session, str(callback.from_user.id))
    await callback.message.edit_text(
        lx.LEXICON_SHOP["shop_text"].format(
            gold=obj.gold,
            stones=obj.stones,
            protection=obj.protection,
            documents=obj.documents,
            antivirus=obj.antivirus,
            active_role=obj.active_role,
            bullet=obj.bullet
        ), reply_markup=shop_keyboard)


@router.callback_query(F.data == "on")
async def profile(callback: CallbackQuery, session: AsyncSession):
    await orm_update_user_profile_on_off(session, str(callback.from_user.id), False)
    obj = await orm_select_user_profile(session, str(callback.from_user.id))
    if obj.on_off:
        await callback.message.edit_text(
            lx.LEXICON_PROFILE["info_user"].format(
                gold=obj.gold,
                stones=obj.stones,
                protection=obj.protection,
                documents=obj.documents,
                antivirus=obj.antivirus,
                active_role=obj.active_role,
                bullet=obj.bullet
            ), reply_markup=profile_keyboard_on
        )
    else:
        await callback.message.edit_text(
            lx.LEXICON_PROFILE["info_user"].format(
                gold=obj.gold,
                stones=obj.stones,
                protection=obj.protection,
                documents=obj.documents,
                antivirus=obj.antivirus,
                active_role=obj.active_role,
                bullet=obj.bullet
            ), reply_markup=profile_keyboard_off
        )


@router.callback_query(F.data == "off")
async def profile(callback: CallbackQuery, session: AsyncSession):
    await orm_update_user_profile_on_off(session, str(callback.from_user.id), True)
    obj = await orm_select_user_profile(session, str(callback.from_user.id))
    if obj.on_off:
        await callback.message.edit_text(
            lx.LEXICON_PROFILE["info_user"].format(
                gold=obj.gold,
                stones=obj.stones,
                protection=obj.protection,
                documents=obj.documents,
                antivirus=obj.antivirus,
                active_role=obj.active_role,
                bullet=obj.bullet
            ), reply_markup=profile_keyboard_on
        )
    else:
        await callback.message.edit_text(
            lx.LEXICON_PROFILE["info_user"].format(
                gold=obj.gold,
                stones=obj.stones,
                protection=obj.protection,
                documents=obj.documents,
                antivirus=obj.antivirus,
                active_role=obj.active_role,
                bullet=obj.bullet
            ), reply_markup=profile_keyboard_off
        )


@router.callback_query(F.data == "shop_gold")
async def pay_one_month(callback: CallbackQuery, session: AsyncSession):
    obj = await orm_select_user_profile(session, str(callback.from_user.id))
    if obj.stones >= 1:
        await orm_update_user_profile_stones(session, str(callback.from_user.id), obj.stones - 1)
        await orm_update_user_profile_gold(session, str(callback.from_user.id), obj.gold + 100)
        obj = await orm_select_user_profile(session, str(callback.from_user.id))
        await callback.message.edit_text(
            lx.LEXICON_SHOP["shop_text"].format(
                gold=obj.gold,
                stones=obj.stones,
                protection=obj.protection,
                documents=obj.documents,
                antivirus=obj.antivirus,
                active_role=obj.active_role,
                bullet=obj.bullet
            ), reply_markup=shop_keyboard)
    else:
        await callback.answer('Не хватает Брюликов!!!')


@router.callback_query(F.data == "shop_protection")
async def pay_one_month(callback: CallbackQuery, session: AsyncSession):
    obj = await orm_select_user_profile(session, str(callback.from_user.id))
    if obj.gold >= 100:
        await orm_update_user_profile_gold(session, str(callback.from_user.id), obj.gold - 100)
        await orm_update_user_profile_protection(session, str(callback.from_user.id), obj.protection + 1)
        obj = await orm_select_user_profile(session, str(callback.from_user.id))
        await callback.message.edit_text(
            lx.LEXICON_SHOP["shop_text"].format(
                gold=obj.gold,
                stones=obj.stones,
                protection=obj.protection,
                documents=obj.documents,
                antivirus=obj.antivirus,
                active_role=obj.active_role,
                bullet=obj.bullet
            ), reply_markup=shop_keyboard)
    else:
        await callback.answer('Не хватает Золота!!!')


@router.callback_query(F.data == "shop_documents")
async def pay_one_month(callback: CallbackQuery, session: AsyncSession):
    obj = await orm_select_user_profile(session, str(callback.from_user.id))
    if obj.gold >= 150:
        await orm_update_user_profile_gold(session, str(callback.from_user.id), obj.gold - 150)
        await orm_update_user_profile_documents(session, str(callback.from_user.id), obj.documents + 1)
        obj = await orm_select_user_profile(session, str(callback.from_user.id))
        await callback.message.edit_text(
            lx.LEXICON_SHOP["shop_text"].format(
                gold=obj.gold,
                stones=obj.stones,
                protection=obj.protection,
                documents=obj.documents,
                antivirus=obj.antivirus,
                active_role=obj.active_role,
                bullet=obj.bullet
            ), reply_markup=shop_keyboard)
    else:
        await callback.answer('Не хватает Золота!!!')


@router.callback_query(F.data == "shop_antivirus")
async def pay_one_month(callback: CallbackQuery, session: AsyncSession):
    obj = await orm_select_user_profile(session, str(callback.from_user.id))
    if obj.gold >= 150:
        await orm_update_user_profile_gold(session, str(callback.from_user.id), obj.gold - 150)
        await orm_update_user_profile_antivirus(session, str(callback.from_user.id), obj.antivirus + 1)
        obj = await orm_select_user_profile(session, str(callback.from_user.id))
        await callback.message.edit_text(
            lx.LEXICON_SHOP["shop_text"].format(
                gold=obj.gold,
                stones=obj.stones,
                protection=obj.protection,
                documents=obj.documents,
                antivirus=obj.antivirus,
                active_role=obj.active_role,
                bullet=obj.bullet
            ), reply_markup=shop_keyboard)
    else:
        await callback.answer('Не хватает Золота!!!')


@router.callback_query(F.data == "shop_active_role")
async def pay_one_month(callback: CallbackQuery, session: AsyncSession):
    obj = await orm_select_user_profile(session, str(callback.from_user.id))
    if obj.stones >= 1:
        await orm_update_user_profile_stones(session, str(callback.from_user.id), obj.stones - 1)
        await orm_update_user_profile_active_role(session, str(callback.from_user.id), obj.active_role + 1)
        obj = await orm_select_user_profile(session, str(callback.from_user.id))
        await callback.message.edit_text(
            lx.LEXICON_SHOP["shop_text"].format(
                gold=obj.gold,
                stones=obj.stones,
                protection=obj.protection,
                documents=obj.documents,
                antivirus=obj.antivirus,
                active_role=obj.active_role,
                bullet=obj.bullet
            ), reply_markup=shop_keyboard)
    else:
        await callback.answer('Не хватает Брюликов!!!')


@router.callback_query(F.data == "shop_bullet")
async def pay_one_month(callback: CallbackQuery, session: AsyncSession):
    obj = await orm_select_user_profile(session, str(callback.from_user.id))
    if obj.stones >= 1:
        await orm_update_user_profile_stones(session, str(callback.from_user.id), obj.stones - 1)
        await orm_update_user_profile_bullet(session, str(callback.from_user.id), obj.bullet + 1)
        obj = await orm_select_user_profile(session, str(callback.from_user.id))
        await callback.message.edit_text(
            lx.LEXICON_SHOP["shop_text"].format(
                gold=obj.gold,
                stones=obj.stones,
                protection=obj.protection,
                documents=obj.documents,
                antivirus=obj.antivirus,
                active_role=obj.active_role,
                bullet=obj.bullet
            ), reply_markup=shop_keyboard)
    else:
        await callback.answer('Не хватает Брюликов!!!')


@router.callback_query(F.data == "shop_1_stones")
@router.callback_query(F.data == "shop_2_stones")
@router.callback_query(F.data == "shop_5_stones")
@router.callback_query(F.data == "shop_10_stones")
async def pay_one_month(callback: CallbackQuery, session: AsyncSession):
    link = {}
    text = ''
    sum_pay = 0
    if callback.data == "shop_1_stones":
        link = pay_yoo.pay(lx.LEXICON_SHOP_SUM["1"], f"Покупка игровой валюты 1 Бриллиант {callback.from_user.id}")
        text = lx.LEXICON_SHOP_BUTTON["shop_1_stones"]
        sum_pay = 1
    elif callback.data == "shop_2_stones":
        link = pay_yoo.pay(lx.LEXICON_SHOP_SUM["2"], f"Покупка игровой валюты 2 Бриллианта {callback.from_user.id}")
        text = lx.LEXICON_SHOP_BUTTON["shop_2_stones"]
        sum_pay = 2
    elif callback.data == "shop_5_stones":
        link = pay_yoo.pay(lx.LEXICON_SHOP_SUM["5"], f"Покупка игровой валюты 5 Бриллиантов {callback.from_user.id}")
        text = lx.LEXICON_SHOP_BUTTON["shop_5_stones"]
        sum_pay = 5
    elif callback.data == "shop_10_stones":
        link = pay_yoo.pay(lx.LEXICON_SHOP_SUM["10"], f"Покупка игровой валюты 10 Бриллиантов {callback.from_user.id}")
        text = lx.LEXICON_SHOP_BUTTON["shop_10_stones"]
        sum_pay = 10
    if link["status"] == "pending":
        keyboard_link = keyboard.generate_all(1, link["url"], **lx.LEXICON_PROFILE_BUTTON_PAY)
        await callback.message.edit_text(text=text, reply_markup=keyboard_link)
        payment = Payment.find_one(link["id"])
        timeout = time.time() + 60 * 10
        f = 0
        while payment.status == "pending":
            if time.time() > timeout:
                f = 1
                break
            payment = Payment.find_one(link["id"])
            print(payment.status)
            await asyncio.sleep(3)
        if payment.status == "succeeded":
            await orm_update_user_profile_stones(session, str(callback.from_user.id), sum_pay)
            obj = await orm_select_user_profile(session, str(callback.from_user.id))
            await callback.message.edit_text(
                lx.LEXICON_SHOP["shop_text"].format(
                    gold=obj.gold,
                    stones=obj.stones,
                    protection=obj.protection,
                    documents=obj.documents,
                    antivirus=obj.antivirus,
                    active_role=obj.active_role,
                    bullet=obj.bullet
                ), reply_markup=shop_keyboard)
        elif f == 1:
            file_name = f"logs/pay_old/pay-{str(datetime.datetime.now().date())}.txt"
            with open(file_name, "a") as file:
                file.write(
                    f"Пополнение прервано по времени - {callback.from_user.id} - link - {link['id']} - {datetime.datetime.now()}\n"
                )
            await callback.message.edit_text(
                "Процесс оплаты был прерван по времени",
                reply_markup=shop_keyboard
            )
        else:
            await callback.message.edit_text(
                "Процесс оплаты был прерван", reply_markup=shop_keyboard
                )
            print("cancel")


@router.message(Command(commands='my_id'))
async def com_help(message: Message):
    await message.answer(text=str(message.from_user.id))


# Этот хэндлер удаляет сообщения которые не обрабатываются
@router.message()
async def delete_warning_message(message: Message):
    print(message.text)
    await message.delete()
