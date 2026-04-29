from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.components.filter_panel import FilterPanel
from src.components.search_bar import SearchBar
from src.components.event_card import EventCard


class EventsPage(BasePage):
    """Page Object for GreenCity Events page."""

    URL = "https://www.greencity.cx.ua/#/greenCity/events"

    EVENT_ITEMS = (By.CSS_SELECTOR, "app-events-list-item")

    def __init__(self, driver):
        super().__init__(driver)
        self.filter_panel = FilterPanel(driver)
        self.search_bar = SearchBar(driver)

    def open(self):
        super().open(self.URL)

    def get_events(self) -> list:
        elements = self.find_all(self.EVENT_ITEMS)
        return [EventCard(self.driver, el) for el in elements]
