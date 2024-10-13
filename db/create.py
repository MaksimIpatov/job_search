import psycopg2

from db.queries import CREATE_TABLE_COMPANIES, CREATE_TABLE_VACANCIES


def create_table_companies(connect_data: dict[str, str]) -> None:
    """Создание таблицы компаний."""
    conn = psycopg2.connect(**connect_data)
    with conn.cursor() as cur:
        print("Создаем таблицу компаний")
        cur.execute(CREATE_TABLE_COMPANIES)
        conn.commit()

    conn.close()


def create_table_vacancies(connect_data: dict[str, str]) -> None:
    """Создание таблицы вакансий."""
    conn = psycopg2.connect(**connect_data)

    with conn.cursor() as cur:
        print("Создаем таблицу вакансий")
        cur.execute(CREATE_TABLE_VACANCIES)
        conn.commit()

    conn.close()
