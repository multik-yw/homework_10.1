import json
from json import JSONDecodeError
from typing import Any


def transactions_function(path_to_file: str) -> str | list[dict] | Any:
    """Преобразование JSON-файла в список словарей:"""
    try:
        with open(path_to_file, encoding="utf-8") as file:
            try:
                operations_data = json.load(file)
            except JSONDecodeError:
                print("Неверные данные JSON.")
                return []
    except FileNotFoundError:
        print("Файл не найден.")
        return []
    return operations_data
