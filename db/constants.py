import json
import os.path
from pathlib import Path

from utils.reader import get_company_names_from_file
from utils.variables import get_env_variables

BASE_DIR = Path(__file__).resolve().parent.parent

DB_VARIABLES: tuple[str, ...] = ("dbname", "user", "password", "host", "port")
CONNECT_DATA: dict[str, str] = get_env_variables(DB_VARIABLES)


COMPANIES_FILE_NAME: str = "companies.json"
COMPANIES_FILE_PATH: str = os.path.join(BASE_DIR, "data", COMPANIES_FILE_NAME)
COMPANIES_DATA: json = get_company_names_from_file(COMPANIES_FILE_PATH)

DELAY_SECONDS: int = 2
API_URL: str = "https://api.hh.ru/vacancies?area=1261"

URL_COMPANIES: str = "{url}&employer_id={company_id}"
URL_VACANCIES: str = "{url}&employer_id={company_id}&page={page}"
URL_PARAMS_FOR_COMPANIES: dict[str, int] = {"page": 0, "per_page": 1}
URL_PARAMS_FOR_VACANCIES: dict[str, int] = {
    "pages": 20,
    "page": 0,
    "per_page": 100,
}

DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"

if __name__ == "__main__":
    print(BASE_DIR)
