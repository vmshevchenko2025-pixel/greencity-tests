import allure
from src.pages.auth_page import AuthPage


@allure.feature("Auth")
@allure.story("Email validation")
class TestInvalidEmail:

    @allure.title("Некоректний email викликає повідомлення про помилку")
    def test_invalid_email_shows_error(self, driver):
        page = AuthPage(driver)

        with allure.step("Відкрити головну сторінку"):
            page.open()

        with allure.step("Відкрити модальне вікно входу"):
            page.open_login_modal()

        with allure.step("Перевірити відображення модального вікна"):
            assert page.is_modal_displayed(), "Модальне вікно повинно відображатись"

        with allure.step("Ввести некоректний email"):
            page.enter_email("test@@gmail")

        with allure.step("Перевірити текст помилки"):
            error_text = page.get_email_error()
            assert "Перевірте, чи правильно вказано вашу адресу електронної пошти" in error_text, \
                f"Очікувалось повідомлення про некоректний email, отримано: '{error_text}'"

    @allure.title("Email без символу @ викликає помилку")
    def test_email_without_at_shows_error(self, driver):
        page = AuthPage(driver)

        with allure.step("Відкрити модальне вікно входу"):
            page.open()
            page.open_login_modal()

        with allure.step("Ввести email без @"):
            page.enter_email("invalidemail.com")

        with allure.step("Перевірити відображення помилки"):
            error_text = page.get_email_error()
            assert error_text, "Повідомлення про помилку повинно бути непорожнім"

    @allure.title("Порожній email не проходить валідацію")
    def test_empty_email_shows_error(self, driver):
        page = AuthPage(driver)

        with allure.step("Відкрити модальне вікно входу"):
            page.open()
            page.open_login_modal()

        with allure.step("Залишити поле email порожнім"):
            page.enter_email("")

        with allure.step("Перевірити відображення помилки"):
            error_text = page.get_email_error()
            assert error_text, "При порожньому email повинна з'явитись помилка"
