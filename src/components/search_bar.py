from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.components.base_component import BaseComponent


class SearchBar(BaseComponent):
    """Search bar component for events page."""

    SEARCH_ICON = (By.CSS_SELECTOR, "div.container-img")
    SEARCH_INPUT = (By.CSS_SELECTOR, "div.container-input input")

    def open(self):
        self.click(self.SEARCH_ICON)

    def search(self, keyword: str):
        self.type(self.SEARCH_INPUT, keyword)
        self.find_visible(self.SEARCH_INPUT).send_keys(Keys.ENTER)
