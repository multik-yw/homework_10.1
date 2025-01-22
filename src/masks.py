import logging
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
full_path_file = os.path.join(base_dir, "logs", "masks.log")

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(full_path_file, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s [%(funcName)s] - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_cart_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    logger.info("Успешное выполнение маскировки карты")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    logger.info("Успешное выполнение маскировки счета")
    return f"**{account_number[-4:]}"


print(get_mask_cart_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))
