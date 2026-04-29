from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent


class Header(BaseComponent):
    """Header navigation component."""

    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".header_navigation-menu-right-list > .header_sign-in-link")

    def click_sign_in(self):
        self.click(self.SIGN_IN_BUTTON)
