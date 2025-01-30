from src.operations import search_by_string, counter_by_description


def test_empty_search_by_string():
    result = search_by_string([], "перевод")
    assert result == [], "Тест не пройден: ожидается []"


def test_search_by_string_register():
    description = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
    ]
    result = search_by_string(description, "перевод")
    assert result == ["{'description': 'Перевод организации'}"], \
        "Тест не пройден: ожидается ['{\'description\': \'Перевод организации\'}']"


def test_search_by_string():
    description = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
    ]
    result = search_by_string(description, "Перевод")
    assert result == ["{'description': 'Перевод организации'}"], \
        "Тест не пройден: ожидается ['{\'description\': \'Перевод организации\'}']"


def test_no_matches_found():
    description = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
    ]
    result = search_by_string(description, "тест")
    assert result == [], "Тест не пройден: ожидается []"


def test_counter_by_description():
    description = [
        {"description": "Перевод организации"},
        {"description": "Открыть вклад"},
    ]
    result = counter_by_description(description, ["Перевод", "вклад"])
    assert result == {"Перевод": 1, "вклад": 1}, "Тест не пройден: ожидается {'Перевод': 1, 'вклад': 1}"


def test_counter_by_description_multiple():
    description = [
        {"description": "Перевод организации "},
        {"description": "Открыть вклад"},
        {"description": "Перевод со счета на счет"},
    ]
    result = counter_by_description(description, ["Перевод", "вклад"])
    assert result == {"Перевод": 2, "вклад": 1}, "Тест не пройден: ожидается {'Перевод': 2, 'вклад': 1}"
