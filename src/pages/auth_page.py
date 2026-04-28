from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.pages.base_page import BasePage


class AuthPage(BasePage):

    URL = "https://www.greencity.cx.ua/#/greenCity"

    # 🔹 Locators
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".header_navigation-menu-right-list > .header_sign-in-link")
    MODAL = (By.XPATH, "//app-auth-modal")
    EMAIL_INPUT = (By.ID, "email")
    EMAIL_ERROR = (By.ID, "email-err-msg")

    # 🔹 Actions
    def open(self):
        self.driver.get(self.URL)

    def open_login_modal(self):
        self.click(self.SIGN_IN_BUTTON)

    def is_modal_displayed(self):
        return self.is_visible(self.MODAL)

    def enter_email(self, email):
        self.type(self.EMAIL_INPUT, email)
        self.find(self.EMAIL_INPUT).send_keys(Keys.TAB)

    def get_email_error(self):
        return self.is_visible(self.EMAIL_ERROR).text
