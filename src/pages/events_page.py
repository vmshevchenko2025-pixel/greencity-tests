from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class EventsPage(BasePage):

    URL = "https://www.greencity.cx.ua/#/greenCity/events"

    # 🔹 Locators
    DATE_FILTER = (By.XPATH, "//*[contains(text(),'Дати')]")
    DATE_CELL = (By.XPATH, "//span[contains(@class,'mat-calendar-body-cell-content') and normalize-space()='2']")
    FILTERED_EVENTS = (By.XPATH, "//div[contains(@class,'active-filter') and contains(@class,'ng-star-inserted')]")

    SEARCH_ICON = (By.CSS_SELECTOR, "div.container-img")
    SEARCH_INPUT = (By.CSS_SELECTOR, "div.container-input input")
    EVENT_ITEMS = (By.CSS_SELECTOR, "app-event-item")

    # 🔹 Actions
    def open(self):
        self.driver.get(self.URL)

    def open_date_filter(self):
        self.click(self.DATE_FILTER)

    def select_date(self):
        self.click(self.DATE_CELL)

    def get_filtered_events(self):
        return self.get_elements(self.FILTERED_EVENTS)

    def open_search(self):
        self.click(self.SEARCH_ICON)

    def search_by_keyword(self, keyword):
        self.type(self.SEARCH_INPUT, keyword)
        self.find(self.SEARCH_INPUT).send_keys(Keys.ENTER)

    def get_search_results(self):
        return self.driver.find_elements(*self.EVENT_ITEMS)