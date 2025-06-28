def test_user_login():
    assert 1 == 1

class TestUserAuthentication:
    def test_login(self):
        assert 1 == 1

def test_assert_positive_case():  # Новый тест, которые проверяет положительный кейс
    assert (2 + 2) == 4  # Ожидается, что тест пройдет


def test_assert_negative_case():  # Новый тест, которые проверяет негативный кейс
    assert (2 + 2) == 5,  "(2 + 2) != 5" # Тут должна быть ошибка