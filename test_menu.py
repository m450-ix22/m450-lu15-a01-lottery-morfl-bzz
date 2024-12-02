from menu import select_menu, show_menu


def test_select_menu_valid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'A')
    assert select_menu() == 'A'
