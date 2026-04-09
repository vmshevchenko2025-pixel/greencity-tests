import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSearchEvents(unittest.TestCase):

    BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(self.BASE_URL)

    def tearDown(self):
        self.driver.quit()

    def test_search_events_by_keyword(self):
        driver = self.driver

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "app-events-list"))
        )

        search_icon = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.container-img"))
        )
        search_icon.click()

        search_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.container-input input"))
        )
        keyword = "eco"
        search_input.clear()
        search_input.send_keys(keyword)
        search_input.send_keys(Keys.ENTER)

        results = []
        for _ in range(60):
            results = driver.find_elements(By.CSS_SELECTOR, "app-event-item")
            if results:
                break
            WebDriverWait(driver, 1).until(lambda d: True)  # чекати 1 сек

        self.assertGreater(len(results), 0, "No events found after search")

        for event in results:
            self.assertIn(keyword.lower(), event.text.lower(), f"Event does not contain '{keyword}': {event.text}")

if __name__ == "__main__":
    unittest.main()