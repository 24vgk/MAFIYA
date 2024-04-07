import os
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from config_bd.BaseModel import Base

from config_data.config import Config, load_config
config: Config = load_config()


engine = create_async_engine(f"mysql+asyncmy://{config.tg_bot.login_bd}:{config.tg_bot.password_bd}@{config.tg_bot.server_bd}:3306/MAFIYA", echo=True)
session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
