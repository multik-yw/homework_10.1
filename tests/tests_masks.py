from src.masks import get_mask_cart_number, get_mask_account
import pytest


@pytest.mark.parametrize("cart_num, expected", [("1234567891234567", "1234 56** **** 4567"),
                                                ("4892456182796315", "4892 45** **** 6315"),
                                                ("5271639784256489", "5271 63** **** 6489"),
                                                ("2378156489123457", "2378 15** **** 3457"),
                                                ("9156472381946728", "9156 47** **** 6728")])
def test_get_mask_cart_number(cart_num, expected):
    assert get_mask_cart_number(cart_num) == expected


@pytest.mark.parametrize("account, mask_account", [("12345678912345678912", "**8912"),
                                                   ("15489624865489566469", "**6469"),
                                                   ("54516494894597262645", "**2645")])
def test_mask_account(account, mask_account):
    assert get_mask_account(account) == mask_account
