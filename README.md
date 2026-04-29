# GreenCity UI Automation Tests

Автоматизовані тести UI для GreenCity на базі Selenium + Pytest + Allure.

## Стек
- Python 3.10+
- Selenium 4.18+
- Pytest 8.0+
- Allure Report

## Встановлення
pip install -r requirements.txt

## Запуск тестів
pytest --alluredir=allure-results

## Allure звіт
allure serve allure-results

## Тестове покриття
- Фільтрація подій за датою
- Пошук подій за ключовим словом
- Валідація некоректного email

## Автор
Valentyna Shevchenko