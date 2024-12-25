from collections.abc import Iterator
from typing import Union


def filter_by_currency(transaction_list: list[dict], currency_code: str = "USD") -> Union[Iterator[dict], str]:
    """
    Функция, принимающая список словарей и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной
    """
    if transaction_list == []:
        return iter([])
    if currency_code not in ["USD"]:
        return "Код валюты не найден"

    for transaction in transaction_list:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction
    return iter([])


def transaction_descriptions(transactions):
    """Генератор, принимающий список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    if transactions == []:
        return "Нет транзакций"

    for description_operation in transactions:
        yield description_operation.get('description')


def card_number_generator(start, stop):
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, stop):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = '0' + card_number
        filtered_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        yield filtered_card_number
