import json
import time

import psycopg2
import requests
from tqdm import tqdm

from db.constants import (
    API_URL,
    DELAY_SECONDS,
    URL_COMPANIES,
    URL_PARAMS_FOR_COMPANIES,
    URL_PARAMS_FOR_VACANCIES,
    URL_VACANCIES,
)
from db.queries import INSERT_INTO_COMPANIES, INSERT_INTO_VACANCIES
from db.utils import extract_vacancy_data


def upload_companies(
    connect_data: dict[str, str],
    companies: json,
    url: str = API_URL,
    delay: int = DELAY_SECONDS,
) -> None:
    """Загружает данные из API hh.ru и заполняет таблицу компании."""
    conn = psycopg2.connect(**connect_data)

    for company, company_id in companies.items():
        print(f"Получаем информацию о компании «{company}»")
        response = requests.get(
            URL_COMPANIES.format(url=url, company_id=company_id),
            URL_PARAMS_FOR_COMPANIES,
        )
        data = response.json()
        if not data.get("items"):
            print(f"Не найдена информация о компании «{company}»")
            continue

        print("Заполняем таблицу компаний")
        with conn.cursor() as cur:
            items: list[tuple[int, str]] = [
                (
                    item.get("employer").get("id"),
                    item.get("employer").get("name"),
                )
                for item in data["items"]
                if company == item.get("employer").get("name")
            ]
            for values in items:
                cur.execute(INSERT_INTO_COMPANIES, values)
            conn.commit()

            time.sleep(delay)
    print("Данные компаний успешно загружены и записаны в базу данных")
    conn.close()


def upload_vacancies(
    connect_data: dict[str, str],
    companies: json,
    url: str = API_URL,
    delay: int = DELAY_SECONDS,
) -> None:
    """Загружает данные из API hh.ru и заполняет таблицу вакансий."""
    conn = psycopg2.connect(**connect_data)

    for company, company_id in companies.items():
        print(f"Загружаем вакансии для «{company}»")
        progress_bar: tqdm = tqdm(
            range(URL_PARAMS_FOR_VACANCIES.get("pages")),
            desc=f"Вакансии в «{company}»",
            bar_format="{l_bar}{bar} {n_fmt}{total_fmt}",
            colour="blue",
            unit="Вакансии",
        )

        for page in progress_bar:
            response = requests.get(
                URL_VACANCIES.format(
                    url=url, company_id=company_id, page=page
                ),
                URL_PARAMS_FOR_VACANCIES,
            )
            data = response.json()
            if not data.get("items"):
                print(f"\nВакансии в «{company}» не найдены")
                continue

            print(
                "\nКоличество найденных вакансий "
                f"{len(data.get('items', []))}"
            )
            print("Заполняем таблицу вакансий")
            with conn.cursor() as cur:
                for vacancy in data.get("items", []):
                    cur.execute(
                        INSERT_INTO_VACANCIES,
                        extract_vacancy_data(vacancy) + (company_id,),
                    )

                conn.commit()
            time.sleep(delay)
    print("Вакансии компаний успешно загружены и записаны в базу данных")
    conn.close()
