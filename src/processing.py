def filters_by_state(list_of_date: list[dict[str, str | int]], value_state: str="EXECUTED") -> list[dict[str, str | int]]:
    """ Функция фильтрует данные по указанному значению """
    filtered_list = []
    for dictionary in list_of_date:
        if dictionary.get("state") == value_state:
            filtered_list.append(dictionary)
    return filtered_list


def sort_by_data(list_of_date: list, is_reverse: bool = True) -> list:
    """ Функция сортировки списка словарей по дате"""
    sorted_list = sorted(list_of_date, key=lambda x: x["data"], reverse=is_reverse)
    return  sorted_list