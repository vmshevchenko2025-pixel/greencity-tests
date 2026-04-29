from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.pages.base_page import BasePage
from src.components.header import Header


class AuthPage(BasePage):
    """Page Object for GreenCity Authentication flow."""

    URL = "https://www.greencity.cx.ua/#/greenCity"

    MODAL = (By.XPATH, "//app-auth-modal")
    EMAIL_INPUT = (By.ID, "email")
    EMAIL_ERROR = (By.ID, "email-err-msg")

    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(driver)

    def open(self):
        super().open(self.URL)

    def open_login_modal(self):
        self.header.click_sign_in()

    def is_modal_displayed(self) -> bool:
        return self.is_visible(self.MODAL)

    def enter_email(self, email: str):
        self.type(self.EMAIL_INPUT, email)
        self.find(self.EMAIL_INPUT).send_keys(Keys.TAB)

    def get_email_error(self) -> str:
        return self.get_text(self.EMAIL_ERROR)
