from selenium.webdriver.common.by import By
from components.base_component import BaseComponent

class EventCard(BaseComponent):

    TITLE = (By.CSS_SELECTOR, "h3")

    def get_title(self):
        return self.find(self.TITLE).text