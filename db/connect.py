import psycopg2

from db.queries import CREATE_DATABASE


def create_database(connect_data: dict[str, str]) -> None:
    dbname: str = connect_data.get("dbname")
    user: str = connect_data.get("user")

    conn = psycopg2.connect(**connect_data)
    print(f'Вы подключились к "{dbname}" как "{user}"')
    cur = conn.cursor()
    conn.autocommit = True

    try:
        print(f'Создание базы данных "{dbname}"')
        cur.execute(CREATE_DATABASE.format(dbname=dbname))
    except psycopg2.errors.DuplicateDatabase:
        print(f'"{dbname}" уже существует')
    else:
        print(f'База данных "{dbname}" успешно создана')
    finally:
        cur.close()
        conn.close()
