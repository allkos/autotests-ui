from playwright.sync_api import sync_playwright, expect
from config import settings
from tools.routes import AppRoute

with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(AppRoute.REGISTRATION)
        registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        expect(registration_email_input).to_be_visible()
        registration_email_input.fill(settings.test_user.email)
        registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        expect(registration_username_input).to_be_visible()
        registration_username_input.fill(settings.test_user.username)
        registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        expect(registration_password_input).to_be_visible()
        registration_password_input.fill(settings.test_user.password)
        registration_button = page.get_by_test_id('registration-page-registration-button')
        expect(registration_button).to_be_visible()
        registration_button.click()
        dashboard = page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard).to_be_visible()
        expect(dashboard).to_have_text("Dashboard")
