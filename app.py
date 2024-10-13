from typing import Callable

from api.manager import DBManager
from db.connect import create_database
from db.constants import COMPANIES_DATA, CONNECT_DATA, DEBUG
from db.create import create_table_companies, create_table_vacancies
from db.upload import upload_companies, upload_vacancies


def helper():
    available_actions: dict[int, str] = {
        1: "Список компаний и количество вакансий у каждой компании",
        2: "Список всех вакансий",
        3: "Средняя зарплата по вакансиям",
        4: "Список вакансий, у которых зарплата выше средней",
        5: "Поиск вакансий по ключевому слову",
    }

    print("Доступные действия:")
    for pos, action in available_actions.items():
        print(f"\t{pos}) {action}")


def run():
    if DEBUG:
        create_database(CONNECT_DATA)
        create_table_companies(CONNECT_DATA)
        create_table_vacancies(CONNECT_DATA)
        upload_companies(CONNECT_DATA, COMPANIES_DATA)
        upload_vacancies(CONNECT_DATA, COMPANIES_DATA)

    database = DBManager(**CONNECT_DATA)
    actions: dict[int, Callable] = {
        1: database.get_companies_and_vacancies_count,
        2: database.get_all_vacancies,
        3: database.get_avg_salary,
        4: database.get_vacancies_with_higher_salary,
        5: database.get_vacancies_with_keyword,
    }

    print('\nДобро пожаловать в "Job Search"\n')
    helper()
    actions_count: int = len(actions)
    while True:
        action: str = input("\nВыберите действие (для выхода 0): ")

        if not action.isdigit():
            print(
                "Пожалуйста, укажите номер действия "
                f"от 1 до {actions_count}"
            )
            continue

        if action == '0':
            break

        action: int = int(action)
        func: Callable = actions.get(action)
        if action == 5:
            by_keyword: str = input("Что будем искать: ")
            result: list[tuple] = func(by_keyword)
            if not result:
                print(f'По вашему запросу "{by_keyword}" ничего не найдено')
        else:
            func()

    print("До встречи!")


if __name__ == "__main__":
    run()
