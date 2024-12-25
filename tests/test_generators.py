from turtledemo.penrose import start

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


def test_filter_by_currency(transactions, cod_curr: str = "USD"):
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


@pytest.mark.parametrize('index, expected', [(0, 'Перевод организации'), (1, 'Перевод со счета на счет')])

def test_transaction_descriptions_3(index, expected):
    transactions = [
        {'description': 'Перевод организации'},
        {'description': 'Перевод со счета на счет'}
    ]
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions[index] == expected


@pytest.mark.parametrize("start, stop, expected", [(2, 3, ["0000 0000 0000 0002"])])
def test_card_number_generator(start, stop, expected):
    assert list(card_number_generator(start, stop)) == expected

