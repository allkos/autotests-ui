from playwright.sync_api import sync_playwright
from tools.routes import AppRoute
from config import settings

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  # Создание контекста
    page = context.new_page() # Создание страницы

    page.goto(AppRoute.REGISTRATION)

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill(settings.test_user.email)

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill(settings.test_user.username)

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill(settings.test_user.password)

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path="browser-state.json")
    from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
    page = context.new_page()

    page.goto(AppRoute.DASHBOARD)
    page.wait_for_timeout(5000)