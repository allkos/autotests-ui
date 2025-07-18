from typing import Pattern

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text
from elements.icon import Icon


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)


        self.icon = Icon(
            page, '{identifier}-drawer-list-item-icon', 'Sidebar item icon'
        )
        self.title = Text(
            page, '{identifier}-drawer-list-item-title-text', 'Sidebar item title'
        )
        self.button = Button(
            page, '{identifier}-drawer-list-item-button', 'Sidebar item button'
        )

    def check_visible(self, title: str, index: str):
        self.icon.check_visible(identifier=index)

        self.title.check_visible(identifier=index)
        self.title.check_have_text(title,identifier=index)

        self.button.check_visible(identifier=index)

    def navigate(self, expected_url: Pattern[str], index: str):
        self.button.click(identifier=index)
        self.check_current_url(expected_url)