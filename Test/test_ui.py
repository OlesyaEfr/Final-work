import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from Pages.ui_class import MainPage

main_page = MainPage

@allure.epic("Читай-город") 
@allure.severity("critical")
@allure.title("Поиск товаров")
@allure.description("Ввод в поисковой строке существующего товара на сайте")
def test_valid_search(driver):
    main_page = MainPage(driver)
    with allure.step("Переходим на стартовую страницу"):
        main_page.go_to_site()
    with allure.step("Вводим наименование товара"):
        driver.find_element(By.CLASS_NAME, "header-search__input").send_keys('шариковая ручка')
    with allure.step("Нажимаем на кнопку поиска"):
        driver.find_element(By.CLASS_NAME, "header-search__button-icon").click()

@allure.epic("Читай-город") 
@allure.severity("critical")
@allure.title("Поиск товаров")
@allure.description("Поиск конкретной книги, которой нет в наличии, и добавление одной из списка в подписки")
def test_add_in_bookmarks(driver):
    main_page = MainPage(driver)
    with allure.step("Переходим на стартовую страницу"):
        main_page.go_to_site()
    with allure.step("Вводим наименование товара"):
        driver.find_element(By.CLASS_NAME, "header-search__input").send_keys('Терри Пратчетт Эрик')
    with allure.step("Нажимаем на кнопку поиска"):
        driver.find_element(By.CLASS_NAME, "header-search__button-icon").click()        
    with allure.step("Ожидание загрузки элемента"):
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((
            By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[1]/div[3]/div[1]')) )
    with allure.step("Скролл к элементу"):
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
    with allure.step("Клик по элементу"):
        ActionChains(driver).move_to_element(element).click(element).perform()

@allure.epic("Читай-город") 
@allure.severity("critical")
@allure.title("Поиск товаров")
@allure.description("Поиск конкретной книги и добавление в корзину")
def test_buy_book(driver):
    main_page = MainPage(driver)
    with allure.step("Переходим на стартовую страницу"):
        main_page.go_to_site()
    with allure.step("Вводим наименование товара"):
        driver.find_element(By.CLASS_NAME, "header-search__input").send_keys('букварь учебное пособие. надежда жукова')
    with allure.step("Нажимаем на кнопку поиска"):
        driver.find_element(By.CLASS_NAME, "header-search__button-icon").click()
    with allure.step("Ожидание загрузки элемента"):
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((
            By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[1]/div[3]/div[1]')) )
    with allure.step("Скролл к элементу"):
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
    with allure.step("Клик по элементу"):
        ActionChains(driver).move_to_element(element).click(element).perform()

@allure.epic("Читай-город") 
@allure.severity("critical")
@allure.title("Кликабельность кнопки")
@allure.description("Проверка перехода в корзину")
def test_cart(driver):
    main_page = MainPage(driver)
    with allure.step("Переходим на стартовую страницу"):
        main_page.go_to_site()
    with allure.step("Переход в корзину"):
        driver.find_element(By.CSS_SELECTOR, ".header-cart.sticky-header__controls-item").click()

@allure.epic("Читай-город") 
@allure.severity("critical")
@allure.title("Кликабельность кнопки")
@allure.description("Проверка перехода в Закладки")
def test_bookmarks(driver):
    main_page = MainPage(driver)
    with allure.step("Переходим на стартовую страницу"):
        main_page.go_to_site()
    with allure.step("Переход в корзину"):
        driver.find_element(By.CSS_SELECTOR, "button[class='header-bookmarks sticky-header__controls-item']").click()
