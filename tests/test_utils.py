from unittest.mock import mock_open, patch

import pytest

from src.utils import transactions_function

@pytest.fixture
def data_for_test_1() -> str:
    return """[
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
]"""


def test_transactions_function_1(data_for_test_1):
    mocked_open = mock_open(read_data=data_for_test_1)
    with patch("builtins.open", mocked_open):
        result = transactions_function("builtins.open")
        assert result == [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        ]


def test_transactions_function_2():
    mocked_open = mock_open(read_data=None)
    with patch("builtins.open", mocked_open):
        result = transactions_function("builtins.open")
        assert result == []


def test_transactions_function_3(capsys):
    param = "[{'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}"
    mocked_open = mock_open(read_data=param)
    with patch("builtins.open", mocked_open):
        print(transactions_function("builtins.open"))
        captured = capsys.readouterr()
        assert captured.out == "JSONDecodeError: Invalid JSON data.\n[]\n"


def test_transactions_function_4():
    param = "[{'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}"
    mocked_open = mock_open(read_data=param)
    with patch("builtins.open", mocked_open):
        result = transactions_function("builtins.open")
        assert result == []


def test_transactions_function_5(capsys):
    print(transactions_function("test.json"))
    captured = capsys.readouterr()
    assert captured.out == "FileNotFoundError: Файл не найден.\n[]\n"


def test_transactions_function_6():
    result = transactions_function("test.json")
    assert result == []
