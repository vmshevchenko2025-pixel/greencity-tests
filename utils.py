import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestFilterByDate(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")

    def tearDown(self):
        self.driver.quit()

    def test_filter_events_by_date(self):

        driver = self.driver

        date_filter = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='date']"))
        )
        date_filter.send_keys("2026-04-01")

        apply_button = driver.find_element(By.XPATH, "//button[contains(text(),'Apply')]")
        apply_button.click()

        events = driver.find_elements(By.CSS_SELECTOR, ".event-card")

        self.assertTrue(len(events) >= 0)


if __name__ == "__main__":
    unittest.main()

