# Руководство по работе с проектом
## Запуск тестов
Предварительные требования
* Python (3.10+)
* Pytest
* Selenium
* Webdriver-manager
* Allure
## Установка библиотек
pip install -r requirements.txt
# Основные команды
## Переход к папке с тестами
  cd "путь к папке с тестами"
## Запуск теста
  python -m pytest
# Параметры запуска
## Запуск теста и генерация отчета
  pytest --alluredir=./allure-result
## Просмотр отчёта
  allure serve reports/allure-results