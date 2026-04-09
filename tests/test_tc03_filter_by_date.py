import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFilterByDate(unittest.TestCase):

    BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.BASE_URL)

    def tearDown(self):
        self.driver.quit()

    def test_filter_by_date(self):
        driver = self.driver

        date_filter = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Дати')]"))
        )
        date_filter.click()

        date = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'mat-calendar-body-cell-content') and normalize-space()='2']"))
        )
        date.click()

        #apply_btn = WebDriverWait(driver, 20).until(
            #EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Apply')]"))
        #)
        #apply_btn.click()

        # Step 4 — Verify results
        events = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[contains(@class,'active-filter') and contains(@class,'ng-star-inserted')]")
            )
        )
        print(f"Found {len(events)} events")

        self.assertTrue(len(events) > 0)


if __name__ == "__main__":
    unittest.main()