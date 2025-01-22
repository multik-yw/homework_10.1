import json
from json import JSONDecodeError
from typing import Any
import logging
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
full_path_file_logs = os.path.join(base_dir, "logs", "utils.log")

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(full_path_file_logs, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s [%(funcName)s] - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def transactions_function(path_to_file: str) -> str | list[dict] | Any:
    """Преобразование JSON-файла в список словарей"""
    try:
        with open(path_to_file, encoding="utf-8") as file:
            try:
                operations_data = json.load(file)
            except JSONDecodeError:
                logger.error("Неверные данные JSON.")
                print("Неверные данные JSON.")
                return []
    except FileNotFoundError:
        logger.error("Файл не найден.")
        print("Файл не найден.")
        return []
    logger.info("Данные успешно получены")
    return operations_data


print(transactions_function('../data/operations.json'))
print(transactions_function(''))
print(transactions_function('masks.py'))
