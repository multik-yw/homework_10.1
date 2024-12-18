from src.masks import get_mask_cart_number, get_mask_account


def mask_account_card(number: str) -> str:
    """Функция маскировки Счета/карты"""
    original_number = number.split()[-1]
    if len(original_number) == 16:
        new_card_number = get_mask_cart_number(original_number)
        result = f"{number[:-16]}{new_card_number}"
    elif len(original_number) == 20:
        new_check_number = get_mask_account(original_number)
        result = f"{number[:-20]}{new_check_number}"
    return result


def get_date(date: str) -> str:
    """Функция преобразования даты в формате ДД.ММ.ГГГГ"""
    new_data = date[0:10].split("-")
    if len(date) != 26:
        raise ValueError("Неверный формат даты")

    return ".".join(new_data[::-1])
