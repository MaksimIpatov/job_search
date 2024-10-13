import psycopg2
from tabulate import tabulate

from api.queries import (
    READ_ALL_VACANCIES,
    READ_COMPANIES_AND_VACANCIES_COUNT,
    READ_VACANCIES_AVG_SALARY,
    READ_VACANCIES_BY_KEYWORD,
    READ_VACANCIES_WITH_HIGHER_SALARY,
)
from db.constants import CONNECT_DATA


class DBManager:
    __instance = None

    def __new__(cls, *args, **kwargs) -> "DBManager":
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, dbname, user, password, host, port) -> None:
        self.__dbname = dbname
        self.__user = user
        self.__password = password
        self.__host = host
        self.__port = port
        self.__show = True

    @property
    def dbname(self) -> str:
        return self.__dbname

    @property
    def port(self) -> str:
        return str(self.__port)

    @property
    def show(self) -> True:
        return self.__show

    @show.setter
    def show(self, value) -> None:
        if value in (True, False):
            self.__show = value

    def __get_connect_data(self) -> dict[str, str]:
        return {
            "dbname": self.__dbname,
            "user": self.__user,
            "password": self.__password,
            "host": self.__host,
            "port": self.__port,
        }

    def print_data(self, data: list[tuple], headers: list[str]) -> None:
        if self.__show:
            print(tabulate(data, headers=headers))

    def get_companies_and_vacancies_count(self) -> list[tuple]:
        """Получает список компаний и количество вакансий у каждой компании."""
        conn = psycopg2.connect(**self.__get_connect_data())

        with conn.cursor() as cur:
            cur.execute(READ_COMPANIES_AND_VACANCIES_COUNT)
            data = cur.fetchall()
            conn.close()

            headers: list[str] = ["Название компании", "Количество вакансий"]
            self.print_data(data, headers)

        return data

    def get_all_vacancies(self) -> list[tuple]:
        """Получает список вакансий."""
        conn = psycopg2.connect(**self.__get_connect_data())

        with conn.cursor() as cur:
            cur.execute(READ_ALL_VACANCIES)
            data = cur.fetchall()
            conn.close()
            headers: list[str] = [
                "Название компании",
                "Название вакансии",
                "Зарплата",
                "Ссылка",
            ]
            self.print_data(data, headers)

        return data

    def get_avg_salary(self) -> list[tuple]:
        """Получает среднюю зарплату по вакансиям."""
        conn = psycopg2.connect(**self.__get_connect_data())

        with conn.cursor() as cur:
            cur.execute(READ_VACANCIES_AVG_SALARY)
            data = cur.fetchall()
            conn.close()

            headers: list[str] = ["Средняя зарплата"]
            self.print_data(data, headers)

        return data

    def get_vacancies_with_higher_salary(self) -> list[tuple]:
        """Получает список всех вакансий.
        У которых зарплата выше средней по всем вакансиям."""
        conn = psycopg2.connect(**self.__get_connect_data())

        with conn.cursor() as cur:
            cur.execute(READ_VACANCIES_WITH_HIGHER_SALARY)
            data = cur.fetchall()
            conn.close()

            headers: list[str] = [
                "Название вакансии",
                "Зарплата",
                "Ссылка",
            ]
            self.print_data(data, headers)

        return data

    def get_vacancies_with_keyword(self, keyword: str) -> list[tuple]:
        """Получает список всех вакансий.
        В названии которых содержатся ключевое слово."""
        conn = psycopg2.connect(**self.__get_connect_data())

        with conn.cursor() as cur:
            cur.execute(
                READ_VACANCIES_BY_KEYWORD.format(keyword=keyword.lower())
            )
            data = cur.fetchall()
            conn.close()

            headers: list[str] = [
                "Название вакансии",
                "Зарплата",
                "Ссылка",
            ]
            self.print_data(data, headers)

        return data


if __name__ == "__main__":
    db_1 = DBManager(**CONNECT_DATA)

    db_1.get_companies_and_vacancies_count()
    # db_1.get_all_vacancies()
    db_1.get_avg_salary()
    # db_1.get_vacancies_with_higher_salary()
    db_1.get_vacancies_with_keyword("Менеджер")
