import pytest
from selenium import webdriver
from pages.auth_page import AuthPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_invalid_email(driver):
    page = AuthPage(driver)

    page.open()
    page.open_login_modal()

    assert page.is_modal_displayed()

    page.enter_email("test@@gmail")
    error_text = page.get_email_error()

    assert "Перевірте, чи правильно вказано вашу адресу електронної пошти" in error_text