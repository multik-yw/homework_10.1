cart_number_str = int()
account_number_str = int()


def get_mask_cart_number(cart_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    return f"{cart_number[:4]} {cart_number[4:6]}** **** {cart_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция максировки номера банковского счета"""
    return f"**{account_number[-4:]}"
