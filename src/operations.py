import re
from collections import Counter

def search_by_string(description: list, search: str) -> list:
    """Принимает список словарей и строку поиска,
     возвращает список словарей, у которых в описании есть эта строка"""
    pattern = search
    new_dict_list = []
    for dictionary in description:
        dict_string = str(dictionary)
        if re.search(pattern, dict_string, flags=re.IGNORECASE):
            new_dict_list.append(dict_string)
    return new_dict_list

def counter_by_description (description: list, operations: list) -> dict:
    """Принимает список словарей и список с категориями
    и возвращает словарь с подсчетом каждой категорий"""
    new_list = []
    for i in operations:
        pattern = i
        description_str = str(description)
        result_string = re.findall(pattern, description_str, flags=re.IGNORECASE)
        new_list = new_list + result_string

    result = Counter(new_list)
    return result
