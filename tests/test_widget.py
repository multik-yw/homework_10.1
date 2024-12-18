from src.widget import mask_account_card, get_date
import pytest


@pytest.mark.parametrize ("value, expected", [("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
                                              ("Visa Platinum 1548626245526465", "Visa Platinum 1548 62** **** 6465")])

def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize ("date, expected", [("2024-03-11T02:26:18.671407", "11.03.2024")])
def test_get_date(date, expected):
    assert get_date(date) == expected

def test_get_date_invalid_date():
    with pytest.raises(ValueError):
       get_date("")