class BaseComponent:
    def __init__(self, driver, root):
        self.driver = driver
        self.root = root

    def find(self, locator):
        return self.root.find_element(*locator)

    def find_all(self, locator):
        return self.root.find_elements(*locator)