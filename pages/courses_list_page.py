from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from components.navigation.sidebar_component import SidebarComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent



class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)


        # Локаторы были заменены компонентом
        self.toolbar_view = CoursesListToolbarViewComponent(page)

        # Карточка курса
        # Меню курса
        self.course_view = CourseViewComponent(page)


        # Пустой блок при отсутствии курсов
        self.empty_view = EmptyViewComponent(page,'courses-list')


    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here',
        )

     # Методы были удалены, т.к. в автотестах будут использоваться методы компонента

