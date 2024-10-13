import json


def get_company_names_from_file(
    filename: str, encoding: str = "UTF-8"
) -> json:
    with open(file=filename, mode="r", encoding=encoding) as data:
        return json.load(data)
