from src.masks import get_mask_cart_number, get_mask_account


def mask_account_card(number: str) -> str:
    """Функция маскировки Счета/карты"""
    if len(number.split()[-1]) == 16:
        new_cart_number = get_mask_cart_number(number.split()[-1])
        result =  f"{number[:16]}{new_cart_number}"
    elif len(number.split()[-1]) == 20:
        new_account_number = get_mask_account(number.split()[-1])
        result = f"{number[:20]}{new_account_number}"
    return result


def get_date(data: str) -> str:
    """Функция преобразования даты в формате ДД.ММ.ГГГГ"""
    new_data = data[0:10].split("-")
    return ".".join(new_data[::-1])
