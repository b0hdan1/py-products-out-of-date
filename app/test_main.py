from unittest import mock
import datetime
import pytest

from app.main import outdated_products


_real_date = datetime.date


@pytest.fixture()
def products_list() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2027, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2026, 10, 17),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2026, 10, 16),
            "price": 160
        }
    ]


@mock.patch("datetime.date")
def test_yesterday_should_return_outdated(
        mocked_date: mock.MagicMock,
        products_list: list
) -> None:
    mocked_date.today.return_value = _real_date(2026, 10, 17)

    mocked_date.side_effect = lambda *args, **kw: _real_date(*args, **kw)
    assert outdated_products(products_list) == ["duck"]


@mock.patch("datetime.date")
def test_today_should_not_return_outdated(
        mocked_date: mock.MagicMock,
        products_list: list
) -> None:
    mocked_date.today.return_value = _real_date(2026, 10, 17)

    mocked_date.side_effect = lambda *args, **kw: _real_date(*args, **kw)
    assert outdated_products(products_list) != ["chicken"]
