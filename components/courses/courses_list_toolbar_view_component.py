import re
import allure

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CoursesListToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page,'courses-list-toolbar-title-text', 'Title')
        self.create_course_button = Button(page,'courses-list-toolbar-create-course-button', 'Create Course')

    @allure.step('Check visible courses list Toolbar')
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Courses')

        self.create_course_button.check_visible()

    def click_create_course_button(self):
        self.create_course_button.click()
        # Дополнительно проверим, что произошел редирект на правильную страницу
        self.check_current_url(re.compile(".*/#/courses/create"))