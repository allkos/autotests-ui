import pytest
from playwright.sync_api import expect, Page, sync_playwright


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):  # Теперь используем фикстуру
        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user@gmail.com')

        username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # context.storage_state(path='browser-state.json')

        dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard_title).to_be_visible()


#    with sync_playwright() as playwright:
#        browser = playwright.chromium.launch(headless=False)
#        context = browser.new_context(storage_state='browser-state.json')
#        page = context.new_page()
#
#        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
#
#       page.wait_for_timeout(5000)
#