# Final-work: pytest_ui_api_"Читай-город"

## Шаблон для автоматизации тестирования на python

## Описание тестируемой системы
**Продукт - Интернет-магазин книг** 

**Сайт** - https://www.chitai-gorod.ru/

«Читай-город» – сеть книжных магазинов, успешно работающих в Москве и других регионах России.

### Стек
- pytest
- selenium
- requests
- allure

### Библиотеки (!)
- pyp install pytest
- pip install selenium
- pip install webdriver-manager
- pip install selenium
- pip install requests
- pip install allure-pytest

### Структура
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API

### Шаги для тестирования

1. Склонировать проект 'git clone https://github.com/OlesyaEfr/Final-work.git
2. Установить зависимости
3. Запустить тесты: 'pytest'- для запуска всех тестов
                    'pytest Test/test_api.py' - для запуска тестов API (ВАЖНО: перед каждым тестированием нужно обновлять токен! Брать из Девтулс-Куки на сайте)
                    'pytest Test/test_ui.py' - для запуска тестов UI
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### Ссылка на финальный проект по ручному тестированию
https://atom-vulture-1e9.notion.site/3edc2ae098314cc783137f3df2df76b8
