from sqlalchemy import create_engine
from config_data.config import Config, load_config
config: Config = load_config()


def engine():
    engine = create_engine(f"mysql+pymysql://{config.tg_bot.login_bd}:{config.tg_bot.password_bd}@{config.tg_bot.server_bd}:3306/MAFIYA", echo=True, pool_recycle=2000)
    return engine


if __name__ == '__main__':
    print(engine())
