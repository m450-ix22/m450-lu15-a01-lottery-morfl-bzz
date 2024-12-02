import pytest
from money import transfer_money, select_transaction
from person import Person


@pytest.fixture
def mock_person():
    return Person("Jane", "securepassword", 50.0)


def test_transfer_money_deposit(mock_person, monkeypatch):
    inputs = iter(['E', '20.0', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    transfer_money(mock_person)
    assert mock_person.balance == 70.0
