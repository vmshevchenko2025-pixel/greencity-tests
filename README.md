# 🧪 GreenCity UI Test Automation Project

## 🎯 Мета проєкту

Цей проєкт створений як практичний етап навчання автоматизації тестування UI.

У процесі роботи реалізовано:
- автоматизацію UI тестів для вебзастосунку GreenCity
- архітектуру **Page Object Model (POM)**
- component-based підхід для повторного використання UI елементів
- генерацію звітів через **Allure Report**

---

## 🛠 Технологічний стек

- **Мова програмування:** Python 3.x  
- **UI автоматизація:** Selenium WebDriver  
- **Тестовий фреймворк:** Pytest  
- **Звітність:** Allure Framework  
- **Архітектура:** Page Object Model + Components  

---

## 📁 Структура проєкту


greencity-tests/
│├── src/
│ ├── pages/ # Page Objects (BasePage, EventsPage, AuthPage)
│ ├── components/ # UI Components (Header, FilterPanel, EventCard)
├── tests/ # Автоматизовані тести
├── conftest.py # Pytest фікстури (driver setup/teardown)
├── pytest.ini # Конфігурація pytest + Allure
├── requirements.txt # Залежності проєкту
└── README.md


---

## ⚙️ Основні принципи архітектури

### 🔹 Page Object Model (POM)
Кожна сторінка інкапсулює:
- локатори
- бізнес-логіку
- методи взаємодії з UI

---

### 🔹 BasePage
Базовий клас сторінок включає:
- роботу з WebDriver
- пошук елементів
- WebDriverWait (Explicit Waits)

---

### 🔹 BaseComponent (обовʼязково)
Базовий клас для UI компонентів:
- доступ до драйвера
- універсальні методи взаємодії
- спільна логіка для всіх компонентів

---

### 🔹 Component-based підхід

UI елементи винесені в окремі компоненти:

- **Header**
- **FilterPanel**
- **EventCard**

👉 Це дозволяє уникнути дублювання коду та підвищує підтримуваність тестів.

---

## 🧪 Тестове покриття

Автоматизовано мінімум 3 тест-кейси:

- перевірка фільтрації подій за датою
- перевірка некоректного email у формі авторизації
- перевірка пошуку подій

---

## 📊 Allure звіти

Для генерації звітів використовується Allure:

### ▶️ Запуск тестів
```bash
pytest --alluredir=allure-results
📊 Генерація звіту
allure serve allure-results
🧑‍🏫 Критерії якості
🔸 Архітектура
чітке розділення Page / Components
відсутність дублювання коду
всі компоненти наслідуються від BaseComponent
🔸 Очікування (Wait Strategy)
❌ заборонено time.sleep()
✅ використовується WebDriverWait (Explicit Waits)
🔸 Локатори
стабільні CSS/XPath локатори
уникнення абсолютних шляхів
використання читабельних селекторів
🔸 Якість коду
відповідність PEP8
зрозуміле іменування змінних і методів
логічна структура проєкту
▶️ Запуск проєкту
1️⃣ Встановлення залежностей
pip install -r requirements.txt
2️⃣ Запуск тестів
pytest
3️⃣ Генерація Allure звіту
pytest --alluredir=allure-results
allure serve allure-results
📌 Definition of Done

✔ Тести працюють стабільно
✔ Використовується POM + Components
✔ Є BasePage та BaseComponent
✔ Немає time.sleep()
✔ Є Allure звітність
✔ Чистий та структурований код
✔ README містить інструкцію запуску
👤 Author

Valentyna Shevchenko
