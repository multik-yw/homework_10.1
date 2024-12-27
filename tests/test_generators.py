from typing import Union, Iterator

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
import pytest


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]


def test_filter_by_currency(transactions:list[dict], cod_curr: str = "USD") -> None:
    generator = filter_by_currency(transactions, cod_curr)
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }

def test_filter_by_currency_error(transactions:list[dict]) -> None:
    gen = filter_by_currency(transactions, '')
    with pytest.raises(StopIteration, match='Код валюты не найден'):
        next(gen)

def test_filter_by_currency_empty(transactions:list[dict]) -> None:
    gen = filter_by_currency([])
    with pytest.raises(StopIteration, match='Список транзакции пуст'):
        next(gen)



@pytest.mark.parametrize('index, expected', [(0, 'Перевод организации'), (1, 'Перевод со счета на счет')])

def test_transaction_descriptions(index:int, expected:str) -> None:
    transactions = [
        {'description': 'Перевод организации'},
        {'description': 'Перевод со счета на счет'}
    ]
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions[index] == expected

def test_transaction_descriptions_error(transactions: list[dict]) -> None:
    if transactions == []:
        assert "Нет транзакций"



@pytest.mark.parametrize("start, stop, expected", [(2, 3, ["0000 0000 0000 0002"])])

def test_card_number_generator(start :int, stop:int, expected:str)-> None:
    assert list(card_number_generator(start, stop)) == expected





