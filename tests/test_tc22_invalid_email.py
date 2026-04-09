import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TestEmailValidation(unittest.TestCase):

    BASE_URL = "https://www.greencity.cx.ua/#/greenCity"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.get(self.BASE_URL)

    def tearDown(self):
        self.driver.quit()

    def test_invalid_email_not_accepted(self):

        driver = self.driver
        wait = self.wait

        sign_in_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".header_navigation-menu-right-list > .header_sign-in-link")
            )
        )
        sign_in_button.click()

        modal = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//app-auth-modal"))
        )
        self.assertTrue(modal.is_displayed(), "Login modal is not displayed")

        email_input = wait.until(
            EC.visibility_of_element_located((By.ID, "email"))
        )
        self.assertTrue(email_input.is_displayed(), "Email input is not displayed")

        email_error = driver.find_element(By.ID, "email-err-msg")
        self.assertFalse(email_error.is_displayed(), "Email error message should not be visible initially")

        invalid_email = "test@@gmail"
        email_input.send_keys(invalid_email)

        email_input.send_keys(Keys.TAB)

        email_error = wait.until(
            EC.visibility_of_element_located((By.ID, "email-err-msg"))
        )

        expected_error = "Перевірте, чи правильно вказано вашу адресу електронної пошти"
        self.assertIn(expected_error, email_error.text)

if __name__ == "__main__":
    unittest.main()