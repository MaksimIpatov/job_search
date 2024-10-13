from random import choices
from string import ascii_letters, digits


def get_random_name_for_db(length: int = 15) -> str:
    """Получение случайного имени для базы данных."""
    _suffix: str = "_db"
    chars: list[str] = choices(
        ascii_letters + digits,
        k=length - len(_suffix),
    )

    return "".join(chars) + _suffix


def process_salary(salary: dict[str, int]) -> int:
    """Обработка зарплаты из данных вакансии."""
    if not salary:
        return 0

    if salary.get("from") and salary.get("to"):
        return int((salary.get("from") + salary.get("to")) / 2)

    return salary.get("from") or salary.get("to")


def extract_vacancy_data(vacancy: dict[str, str | int | dict]) -> tuple:
    """Извлечение данных о вакансии в виде кортежа."""
    hh_id = vacancy.get("id")
    vacancy_name = vacancy.get("name")
    vacancy_url = vacancy.get("alternate_url")
    salary = process_salary(vacancy.get("salary"))
    schedule = vacancy.get("schedule", {}).get("name")

    return hh_id, vacancy_name, vacancy_url, salary, schedule


if __name__ == "__main__":
    print(get_random_name_for_db())
