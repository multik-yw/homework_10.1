from collections.abc import Iterator
from typing import Union


#def filter_by_currency(my_list: list[dict], currency_code: str = "USD") -> Union[Iterator[dict], str]:
  #  """
  #  Функция, которая принимает на вход список словарей.
  #  Функция должна возвращать итератор, который поочередно выдает транзакции,
  #  где валюта операции соответсвует заданной (например, USD)
   # """
  #  if my_list == []:
  #      return iter([])
   # if currency_code not in ["USD"]:
  #      return "Код валюты не найден"

  #  for transaction in my_list:
   #     if transaction["operationAmount"]["currency"]["code"] == currency_code:
   #         yield transaction
   #     return iter([])

def filter_by_currency(transaction_list:Union[list, dict], currency: str) -> Union[Iterator[dict], str]:
    """
    Функция, принимающая список словарей и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной
    """
    filtered_expression = filter(lambda x: x["currency"]["code"] == currency, transaction_list)
    return filtered_expression


def transaction_descriptions(list_of_transaction:Union[list, dict]) -> Union[Iterator[dict], str]:
    """Генератор, принимающий список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    id_transaction = filter(lambda x: x["id"] is True, list_of_transaction)
    descriptions_transaction = filter(lambda x: x["descriptions"] is True, list_of_transaction)
    while True:
        print(id_transaction["id"])
        yield descriptions_transaction["descriptions"]

def card_number_generator(start, stop):
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, stop):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = '0' + card_number
        filtered_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        yield filtered_card_number


