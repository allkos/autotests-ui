from playwright.sync_api import sync_playwright, expect
from config import settings
from tools.routes import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(AppRoute.REGISTRATION)
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill(settings.test_user.email)
    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill(settings.test_user.username)
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill(settings.test_user.password)
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).not_to_be_disabled()


