from typing import Iterator, Union


def filter_by_currency(transaction_list: list[dict], currency_code: str = "USD") -> Union[Iterator[dict], str]:
    """
    Функция, принимающая список словарей и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной
    """
    if transaction_list == []:
        return "Список транзакции пуст"
    elif currency_code not in ["USD", "RUB"]:
        return "Код валюты не найден"

    for transaction in transaction_list:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction
    return iter([])


def transaction_descriptions(transactions: list[dict]) -> Union[Iterator[dict], str]:
    """Генератор, принимающий список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    if transactions == []:
        return "Нет транзакций"

    for description_operation in transactions:
        yield description_operation.get('description')
    return iter([])


def card_number_generator(start: int, stop: int) -> Union[Iterator[dict], str]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, stop + 1):
        card_number = f"{number:016}"
        filtered_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield filtered_card_number
        return iter([])
    return None
