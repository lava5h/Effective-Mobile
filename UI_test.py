import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages.UI_page import ClickButtons
from allure import step

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
click_buttons = ClickButtons(driver)

# Функция клика по блокам
def test_click_buttons():
    
    # Cписок блоков
    Locators = [
    "div[data-elem-id='1680606406481'] a.tn-atom",
    "div[data-elem-id='1680606406485'] a.tn-atom",
    "div[data-elem-id='1680606406489'] a.tn-atom",
    "div[data-elem-id='1706704571141'] a.tn-atom",
    "div[data-elem-id='1680606406492'] a.tn-atom",
    "div[data-elem-id='1680606406495'] a.tn-atom",
    "div[data-elem-id='1680606406475'] div.tn-atom a[href='#main']"]

    for locator in Locators:
        with step(f"Клик по элементу с локатором: {locator}"):
            click_buttons.clickbutton(locator)
    
    driver.quit()
