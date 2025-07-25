import pytest
import allure
from allure_commons.types import Severity

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.routes import AppRoute
from config import settings



@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)  # Добавили теги
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.feature(AllureFeature.AUTHENTICATION) # Добавили feature
@allure.story(AllureStory.REGISTRATION) # Добавили story
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @allure.title("Registration with correct email, username and password") # Добавили заголовок
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self, dashboard_page: DashboardPage, registration_page: RegistrationPage):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
