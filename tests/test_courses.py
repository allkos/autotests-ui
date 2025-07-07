import pytest
from playwright.sync_api import sync_playwright, expect, Page

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_button = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_button).to_be_visible()
        expect(courses_button).to_have_text("Courses")
        courses_list = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(courses_list).to_be_visible()
        expect(courses_list).to_have_text("There is no results")
        icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(icon).to_be_visible()
        description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(description).to_be_visible()
        expect(description).to_have_text("Results from the load test pipeline will be displayed here")

