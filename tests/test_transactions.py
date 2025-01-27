from unittest.mock import patch

import pandas as pd

from src.transactions import transactions_csv, transactions_excel


def test_transactions_csv() -> None:
    with patch('pandas.read_csv') as mock_read_csv:
        mock_data = pd.DataFrame(columns=['date', 'amount', 'description'])
        mock_read_csv.return_value = mock_data
        result = transactions_csv('some_file.csv')
        expected_result = []
        assert result == expected_result
        mock_read_csv.assert_called_once_with('some_file.csv', sep=';')


def test_transactions_excel() -> None:
    with patch('pandas.read_excel') as mock_read_excel:
        mock_data = pd.DataFrame(columns=['date', 'amount', 'description'])
        mock_read_excel.return_value = mock_data
        result = transactions_excel('some_file.excel')
        expected_result = []
        assert result == expected_result
        mock_read_excel.assert_called_once_with('some_file.excel')


def test_transactions_csv_error() -> None:
    assert transactions_csv("test") == "Файл не найден"


def test_transactions_excel_error() -> None:
    assert transactions_excel("test") == "Файл не найден"
