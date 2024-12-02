import pytest
from lottery import create_ticket, Ticket
from person import Person


@pytest.fixture
def mock_person():
    person = Person("John", "password", 10.0)
    person.tickets = []
    return person


def test_create_ticket_success(mock_person, monkeypatch):
    inputs = iter(['1', '2', '3', '4', '5', '6', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    create_ticket(mock_person)
    assert mock_person.balance == 8.0
    assert len(mock_person.tickets) == 1
