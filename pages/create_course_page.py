from playwright.sync_api import Page, expect

from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.create_exercise_form = CreateCourseExerciseFormComponent(page)
        self.create_course_form = CreateCourseFormComponent(page)
        self.exercises_toolbar_view = CreateCourseExercisesToolbarViewComponent(page)
        self.course_toolbar_view = CreateCourseToolbarViewComponent(page)



    def check_visible_create_course(self):
        self.course_toolbar_view.check_visible()

    def click_create_course_button(self):
        self.course_toolbar_view.click_create_course_button()


    def check_visible_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.create_course_form.check_visible(title, estimated_time,description,max_score,min_score)

    def fill_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.create_course_form.fill(title, estimated_time, description, max_score, min_score)

    def check_visible_exercises(self):
        self.exercises_toolbar_view.check_visible()


    def click_create_exercise_button(self):
        self.exercises_toolbar_view.click_create_exercise_button()

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )