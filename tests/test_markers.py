import pytest

@pytest.mark.smoke
def test_smoke_case():
    assert 1 + 1 == 2

@pytest.mark.regression
def test_regression_case():
    assert 2 * 2 == 4

@pytest.mark.ui
class TestUserInterface:

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_button(self):
        pass

    @pytest.mark.regression
    def test_forgot_password_link(self):
        pass

    @pytest.mark.smoke
    def test_signup_form(self):
        pass