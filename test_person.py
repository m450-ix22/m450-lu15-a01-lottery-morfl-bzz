from person import Person


def test_person_properties():
    person = Person("Alice", "secret", 20.0)
    assert person.givenname == "Alice"
    assert person.password == "secret"
    assert person.balance == 20.0
