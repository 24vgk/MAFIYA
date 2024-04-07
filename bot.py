import asyncio
import logging
import logging.config
from datetime import datetime

from config_bd.engine import create_db, session_maker
from logging_data.logging_settings import logging_config
from aiogram import Bot, Dispatcher
from aiogram_dialog import setup_dialogs
from config_data.config import Config, load_config
from handlers import other_handlers, sheduler_distribution
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from keyboards.set_menu import set_main_menu
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler_di import ContextSchedulerDecorator
from middlewares.apscheduler_m import SchedulerMiddleware

# Инициализируем логгер
from middlewares.db import DataBaseSession

logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main() -> None:
    # Кофигурируем логирование с помощью словаря
    logging.config.dictConfig(logging_config)

    # Выводим в консоль информацию о начале запуска
    logger.info('Starting BOTV')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    storage = RedisStorage.from_url('redis://localhost:6379/0', key_builder=DefaultKeyBuilder(with_destiny=True))
    dp: Dispatcher = Dispatcher(storage=storage)
    jobstores = {
        'default': RedisJobStore(
            jobs_key='dispatched_trips_jobs',
            run_times_key='dispatched_trips_running',
            host='localhost',
            db=2,
            port=6379
        )
    }

    # Настраиваем кнопку Menu
    await set_main_menu(bot)
    # Сообщения по расписанию
    scheduler = ContextSchedulerDecorator(AsyncIOScheduler(timezone="Europe/Moscow", jobstores=jobstores))
    scheduler.ctx.add_instance(bot, declared_class=Bot)
    scheduler.start()
    try:
        scheduler.remove_job('random')
    except:
        pass
    scheduler.add_job(sheduler_distribution.random, id='random', trigger='cron', hour=00,
                      minute=1, start_date=datetime.now())
    await create_db()

    # Регистриуем роутеры в диспетчере
    dp.update.middleware(DataBaseSession(session_pool=session_maker))
    dp.update.middleware.register(SchedulerMiddleware(scheduler))
    dp.include_router(other_handlers.router)
    setup_dialogs(dp)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    except Exception as ex:
        logging.error(f'[Exception] - {ex}', exc_info=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
