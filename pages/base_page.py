from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, ElementClickInterceptedException


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            timeout,
            poll_frequency=0.5,
            ignored_exceptions=(StaleElementReferenceException,)
        )

    # -------------------------
    # OPEN PAGE
    # -------------------------
    def open(self, url):
        self.driver.get(url)

    # -------------------------
    # FIND
    # -------------------------
    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    # -------------------------
    # SAFE CLICK (MAIN METHOD)
    # -------------------------
    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            return element
        except ElementClickInterceptedException:
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)
            return element

    # -------------------------
    # JS CLICK (FALLBACK ONLY)
    # -------------------------
    def js_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)
        return element

    # -------------------------
    # SAFE TYPE
    # -------------------------
    def type(self, locator, text, clear=True):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        if clear:
            element.clear()
        element.send_keys(text)
        return element

    # -------------------------
    # WAIT FOR ELEMENT
    # -------------------------
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    # -------------------------
    # WAIT FOR CLICKABLE
    # -------------------------
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    # -------------------------
    # SAFE EXISTS
    # -------------------------
    def is_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False