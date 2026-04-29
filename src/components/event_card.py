from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent


class EventCard(BaseComponent):
    """Represents a single event card on the events listing page."""

    TITLE = (By.CSS_SELECTOR, "h3, .event-title")

    def __init__(self, driver, element):
        super().__init__(driver)
        self.element = element

    def get_title(self) -> str:
        elements = self.element.find_elements(*self.TITLE)
        return elements[0].text if elements else self.element.text

    def get_full_text(self) -> str:
        return self.element.text
