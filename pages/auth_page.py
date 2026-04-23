from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class AuthPage(BasePage):

    URL = "https://www.greencity.cx.ua/#/greenCity"

    SIGN_IN_BTN = (By.XPATH, "//a[contains(@class,'header_sign-in-link') and not(contains(@style,'display: none'))]")
    EMAIL_INPUT = (By.ID, "email")
    EMAIL_ERROR = (By.ID, "email-err-msg")

    def open_page(self):
        self.open(self.URL)

    def open_login_modal(self):
        btn = self.wait.until(
            EC.visibility_of_element_located(self.SIGN_IN_BTN)
        )
        self.driver.execute_script("arguments[0].click();", btn)

    def enter_email(self, email):
        self.find(self.EMAIL_INPUT).send_keys(email)

    def get_email_error(self):
        return self.find(self.EMAIL_ERROR).text