import time
from sqlalchemy import insert, select, update, MetaData, Table, delete
import config_bd.BaseModel as e


class SQL:

    def __init__(self):
        self.engine = e.engine()
        metadata = MetaData()
        self.Users = Table('Users', metadata, autoload_replace=True, autoload_with=self.engine)

    def INSERT(
            self, telegram_id: int,
            balance: int = 0,
            count_active_key: int = 0,
            count_key: int = 0,
            position_funnel: int = 0,
            count_ref: int = 0,
            count_ref_pay: int = 0,
            ref: str = "0",
            is_admin: bool = False,
            check_in: bool = False,
            login: str = None,
            user_name: str = None
    ) -> None:
        """
        Добавляет пользователей в Users.
        """
        conn = self.engine.connect()
        try:
            ins = insert(self.Users).values(
                telegram_id=telegram_id,
                balance=balance,
                count_active_key=count_active_key,
                count_key=count_key,
                position_funnel=position_funnel,
                count_ref=count_ref,
                count_ref_pay=count_ref_pay,
                ref=ref,
                is_admin=is_admin,
                check_in=check_in,
                login=login,
                user_name=user_name
            )
            conn.execute(ins)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            print(str(e))
            self.engine.dispose()

    def UPDATE_Login(self, telegram_id: int, login: str) -> None:
        """
        Метод изменения данных в колонке login
        :param telegram_id: int
        :param login: str
        :return: None
        """
        conn = self.engine.connect()
        try:
            s = update(self.Users).where(self.Users.c.telegram_id == telegram_id).values(login=login)
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def UPDATE_username(self, telegram_id: int, user_name: str) -> None:
        """
        Метод изменения данных в колонке username
        :param telegram_id: int
        :param username: str
        :return: None
        """
        conn = self.engine.connect()
        try:
            s = update(self.Users).where(self.Users.c.telegram_id == telegram_id).values(user_name=user_name)
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def UPDATE_BALANCE(self, telegram_id: int, balance: float) -> None:
        """
        Метод изменения данных в колонке Баланса
        :param telegram_id: int
        :param balance: float
        :return: None
        """
        conn = self.engine.connect()
        try:
            s = update(self.Users).where(self.Users.c.telegram_id == telegram_id).values(balance=balance)
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def SELECT_ALL(self) -> set[list]:
        """
        Получаем кортеж всех строк таблицы Users в виде списков
        :return: set(list)
        """
        conn = self.engine.connect()
        try:
            s = select(self.Users)
            re = conn.execute(s)
            result = re.fetchall()
            conn.commit()
            conn.close()
            self.engine.dispose()
            return result
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def SELECT_USER(self, telegram_id: int) -> list:
        """
        Получаем строку из таблицы Users в виде списка колонок
        :return: list
        """
        conn = self.engine.connect()
        try:
            s = select(self.Users).where(self.Users.c.telegram_id == telegram_id)
            re = conn.execute(s)
            result = re.fetchall()
            conn.commit()
            conn.close()
            self.engine.dispose()
            return result[0]
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def UPDATE_CHECK_IN(self, telegram_id: int, check_in: bool) -> None:
        """
        Метод изменения данных в колонке CHECK_IN
        :param telegram_id: int
        :param check_in: bool
        :return: None
        """
        conn = self.engine.connect()
        try:
            s = update(self.Users).where(self.Users.c.telegram_id == telegram_id).values(check_in=check_in)
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def UPDATE_COUNT_ACTIVE_KEY(self, telegram_id: int, count_active_key: int) -> None:
        """
        Метод изменения данных в колонке COUNT_ACTIVE_KEY
        :param telegram_id: int
        :param count_active_key: int
        :return: None
        """
        conn = self.engine.connect()
        try:
            s = update(self.Users).where(self.Users.c.telegram_id == telegram_id).values(count_active_key=count_active_key)
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def UPDATE_COUNT_KEY(self, telegram_id: int, count_key: int) -> None:
        """
        Метод изменения данных в колонке COUNT_KEY
        :param telegram_id: int
        :param count_key: int
        :return: None
        """
        conn = self.engine.connect()
        try:
            s = update(self.Users).where(self.Users.c.telegram_id == telegram_id).values(count_key=count_key)
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def UPDATE_POSITION_FUNNEL(self, telegram_id: int, position_funnel: int) -> None:
        """
        Метод изменения данных в колонке position_funnel
        :param telegram_id: int
        :param position_funnel: int
        :return: None
        """
        conn = self.engine.connect()
        try:
            s = update(self.Users).where(self.Users.c.telegram_id == telegram_id).values(position_funnel=position_funnel)
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def UPDATE_COUNT_REF(self, telegram_id: str, count_ref: int) -> None:
        """
        Метод изменения данных в колонке count_ref
        :param telegram_id: str
        :param count_ref: int
        :return: None
        """
        conn = self.engine.connect()
        try:
            s = update(self.Users).where(self.Users.c.telegram_id == telegram_id).values(count_ref=count_ref)
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def UPDATE_COUNT_REF_PAY(self, telegram_id: str, count_ref_pay: int) -> None:
        """
        Метод изменения данных в колонке count_ref_pay
        :param telegram_id: str
        :param count_ref_pay: int
        :return: None
        """
        conn = self.engine.connect()
        try:
            s = update(self.Users).where(self.Users.c.telegram_id == telegram_id).values(count_ref_pay=count_ref_pay)
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def UPDATE_REF(self, telegram_id: int, ref: str) -> None:
        """
        Метод изменения данных в колонке ref
        :param telegram_id: int
        :param ref: str
        :return: None
        """
        conn = self.engine.connect()
        try:
            s = update(self.Users).where(self.Users.c.telegram_id == telegram_id).values(ref=ref)
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def UPDATE_IS_ADMIN(self, telegram_id: int, is_admin: bool) -> None:
        """
        Метод изменения данных в колонке is_admin
        :param telegram_id: int
        :param is_admin: bool
        :return: None
        """
        conn = self.engine.connect()
        try:
            s = update(self.Users).where(self.Users.c.telegram_id == telegram_id).values(is_admin=is_admin)
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def UPDATE_CHECK_AUTO_PAY(self, telegram_id: int, check_auto_pay: bool) -> None:
        """
        Метод изменения данных в колонке check_auto_pay
        :param telegram_id: int
        :param check_auto_pay: bool
        :return: None
        """
        conn = self.engine.connect()
        try:
            s = update(self.Users).where(self.Users.c.telegram_id == telegram_id).values(check_auto_pay=check_auto_pay)
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def UPDATE_CHECK_FIRST_PAY(self, telegram_id: int, check_first_pay: bool) -> None:
        """
        Метод изменения данных в колонке check_first_pay
        :param telegram_id: int
        :param check_first_pay: bool
        :return: None
        """
        conn = self.engine.connect()
        try:
            s = update(self.Users).where(self.Users.c.telegram_id == telegram_id).values(check_first_pay=check_first_pay)
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def UPDATE_COUNT_KEY_PC(self, telegram_id: int, count_key_pc: int) -> None:
        """
        Метод изменения данных в колонке count_key_pc
        :param telegram_id: int
        :param count_key_pc: int
        :return: None
        """
        conn = self.engine.connect()
        try:
            s = update(self.Users).where(self.Users.c.telegram_id == telegram_id).values(count_key_pc=count_key_pc)
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def UPDATE_COUNT_KEY_M(self, telegram_id: int, count_key_m: int) -> None:
        """
        Метод изменения данных в колонке count_key_m
        :param telegram_id: int
        :param count_key_m: int
        :return: None
        """
        conn = self.engine.connect()
        try:
            s = update(self.Users).where(self.Users.c.telegram_id == telegram_id).values(count_key_m=count_key_m)
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def DELETE_USER(self, telegram_id: str) -> None:
        """
        """
        conn = self.engine.connect()
        try:
            s = delete(self.Users).where(self.Users.c.telegram_id == telegram_id)
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))


if __name__ == '__main__':
    s = SQL()
    s.INSERT(24362636728478)