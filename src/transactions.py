import pandas as pd


def transactions_csv(file: str) -> list | str:
    """Считывание финансовых операций из CSV."""
    try:
        df = pd.read_csv(file, sep=';')
        result = df.to_dict(orient='records')
    except FileNotFoundError:
        return ("Файл не найден")
    else:
        return result


def transactions_excel(file_path: str) -> list | str:
    """Считывание финансовых операций из Excel."""
    try:
        df = pd.read_excel(file_path)
        result = df.to_dict(orient='records')
    except FileNotFoundError:
        return ("Файл не найден")
    else:
        return result
