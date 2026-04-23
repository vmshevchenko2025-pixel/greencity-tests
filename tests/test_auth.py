from pages.auth_page import AuthPage

def test_invalid_email(driver):
    page = AuthPage(driver)

    page.open_page()
    page.open_login_modal()
    page.enter_email("test@@gmail")

def trigger_validation(self):
    self.find(self.EMAIL_INPUT).send_keys(Keys.TAB)


    error = page.get_email_error()

    assert "Перевірте" in error


