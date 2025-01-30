def filters_by_state(list_of_date: list[dict[str, str | int]], value: str = "EXECUTED") -> list[dict[str, str | int]]:
    """ Функция фильтрует данные по указанному значению """
    return [i for i in list_of_date if i.get("state") == value]


def sort_by_data(list_of_date: list, is_reverse: bool = True) -> list:
    """ Функция сортировки списка словарей по дате"""
    return sorted(list_of_date, key=lambda list_dictionaries: list_dictionaries["date"], reverse=is_reverse)

