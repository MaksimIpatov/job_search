import os

from dotenv import load_dotenv

load_dotenv()


def validate_env_variables(variables: dict[str, str]) -> None:
    _required_variables: tuple[str, ...] = (
        "dbname",
        "user",
        "password",
        "host",
        "port",
    )
    invalid_variables: list[str] = [
        item for item in _required_variables if item not in variables
    ]
    if invalid_variables:
        raise AttributeError(f"Укажите {', '.join(invalid_variables)}")

    invalid_variables: list[str] = [
        key for key, value in variables.items() if not value
    ]
    if invalid_variables:
        raise ValueError(
            f"Убедитесь, что для {', '.join(invalid_variables)} "
            "указаны значения",
        )


def get_env_variables(
    variables: list[str] | tuple[str, ...]
) -> dict[str, str]:
    data: dict[str, str] = {}
    for key in variables:
        data[key] = os.getenv(key)

    validate_env_variables(data)

    return data
