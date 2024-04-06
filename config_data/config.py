from __future__ import annotations

from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота
    yoo_id: str
    yoo_token: str
    login_bd: str
    password_bd: str
    server_bd: str



@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:

    env: Env = Env()
    env.read_env(path)

    return Config(tg_bot=TgBot(token=env('BOTV_TOKEN'),
                               admin_ids=list(map(int, env.list('ADMIN_IDS'))),
                               yoo_id=env('yoo_id'),
                               yoo_token=env('yoo_token'),
                               login_bd=env('login_bd'),
                               password_bd=env('password_bd'),
                               server_bd=env('server_bd'),
                               )
                  )

