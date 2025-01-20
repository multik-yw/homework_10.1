import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
apilayer_key = os.getenv("API_KEY")


test_transaction = {
    "id": 179194306,
    "state": "EXECUTED",
    "date": "2019-05-19T12:51:49.023880",
    "operationAmount": {"amount": "6381.58", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "МИР 5211277418228469",
    "to": "Счет 58518872592028002662",
}


def conversion_function(transaction: dict) -> Any:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    try:
        currency = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
    except KeyError:
        return "Отсутствуют необходимые данные"
    exchange_rates_data_api = os.getenv("API_KEY")
    if currency == "USD" or currency == "EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": exchange_rates_data_api}
        response = requests.get(url, headers=headers)
        result = response.json()
        print(result)
        return result["result"]
    else:
        return "Неподходящая валюта для конвертации"
