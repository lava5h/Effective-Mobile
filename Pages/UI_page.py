from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class ClickButtons:

    """
    Класс для перехода по блокам.
    
    Этот класс позволяет переходить по всем блокам.
    """
    # Функция инициализации страницы
    def __init__(self, driver):

        """
        Инициализация страницы.

        driver: объект веб-драйвера.
        """

        self.driver = driver
        self.driver.get("https://effective-mobile.ru")

    # Функция клика по блокам 
    def clickbutton(self, locator):

        """
        Переход по блокам.

        Метод выполняет переход по каждому блоку.
        """

        button = self.driver.find_element(By.CSS_SELECTOR, locator)
        button.click()
