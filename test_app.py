from app import add, is_valid_user

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_user_validation():
    assert is_valid_user("admin") is True
    assert is_valid_user("ab") is False
