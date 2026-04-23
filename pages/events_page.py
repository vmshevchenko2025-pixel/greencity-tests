from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class EventsPage(BasePage):

    DATE_FILTER_BTN = (By.XPATH, "//*[contains(text(),'Date range')]")
    EVENTS = (By.CSS_SELECTOR, ".event-card")

    def open_page(self):
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")

    def filter_by_date(self, day="2"):
        self.click(self.DATE_INPUT)

        day_locator = (By.XPATH, f"//td[contains(@class,'mat-calendar-body-cell') and .//text()='{day}']")

        self.wait_clickable(day_locator).click()