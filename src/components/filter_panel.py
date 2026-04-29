from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.components.base_component import BaseComponent


class FilterPanel(BaseComponent):
    """Filter panel component for events page.

    Real DOM structure (from DevTools inspection):
    <div class="dropdown" tabindex="0">
      <mat-label class="filter">Date range</mat-label>
      <mat-date-range-input ...>
      <mat-date-range-picker class="custom-calendar">
    </div>
    """

    DATE_RANGE_DROPDOWN = (
        By.XPATH,
        "//*[contains(text(),'Дати')]"
    )
    CALENDAR_FIRST_AVAILABLE = (
        By.XPATH,
        "(//td[contains(@class,'mat-calendar-body-cell') and "
        "not(contains(@class,'mat-calendar-body-disabled'))])[1]"
    )
    ACTIVE_FILTERS = (By.CSS_SELECTOR, "[class*='active-filter']")

    def open_date_filter(self):
        """Open date range picker via JS click (Angular Material div)."""
        element = self.wait.until(EC.presence_of_element_located(self.DATE_RANGE_DROPDOWN))
        self.driver.execute_script("arguments[0].click();", element)

    def select_date_cell(self):
        """Select first available date in the open calendar."""
        element = self.wait.until(EC.presence_of_element_located(self.CALENDAR_FIRST_AVAILABLE))
        self.driver.execute_script("arguments[0].click();", element)

    def get_active_filters(self):
        try:
            return self.find_all(self.ACTIVE_FILTERS)
        except Exception:
            return []
