import pytest
import allure

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.routes import AppRoute
from config import settings


@pytest.mark.courses
@pytest.mark.regression
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.visit(AppRoute.CREATE_COURSE)

    create_course_page.create_course_toolbar_view.check_visible()
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
    create_course_page.create_course_form.check_visible(
        title="", max_score="0", min_score="0", description="", estimated_time=""
    )

    create_course_page.create_course_exercises_toolbar_view.check_visible()
    create_course_page.check_visible_exercises_empty_view()

    create_course_page.image_upload_widget.upload_preview_image(file=settings.test_data.image_png_file)
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
    create_course_page.create_course_form.fill(
        title="Playwright",
        max_score="100",
        min_score="10",
        description="Playwright",
        estimated_time="2 weeks"
    )
    create_course_page.create_course_toolbar_view.click_create_course_button()

    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible(
        index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
    )
