from src.processing import filters_by_state, sort_by_data
import pytest


@pytest.fixture
def operations() -> list[dict]:
    transactions = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    return transactions


@pytest.fixture
def executed_operations() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},

    ]


@pytest.fixture
def canceled_operations() -> list[dict]:
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize("operation, state, result", [
    ('operations', None, 'executed_operations'),
    ('operations', "EXECUTED", 'executed_operations'),
    ('operations', "CANCELED", 'canceled_operations')
])
def test_filters_by_state_normal(operation: list[dict], state: str, result: list[dict], request) -> None:
    state = state if state is not None else "EXECUTED"
    assert filters_by_state(request.getfixturevalue(operation), state) == request.getfixturevalue(result)


@pytest.fixture
def test_sort_by_data(state):
    assert sort_by_data(state) == [{"id": 939719570, "state": "EXECUTED", "data": "2018-06-30T02:08:58.425572"},
                                   {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                                   {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                                   {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]


@pytest.fixture
def test_sort_by_data(list_of_date, sorted_list):
    assert sort_by_data(list_of_date) == sorted_list
