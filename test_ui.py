from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture 
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()



#1.Ввод в поисковой строке существующего товара на сайте
#driver.find_element(By.TAG_NAME, input).send_keys('python')
#driver.find_element(By.XPATH, html[1]body[1]div[2]div[1]div[1]header[1]div[1]div[1]div[2]div[1]form[1]button[1][name()='svg'][1]).click()

#sleep(5)

#2.Поиск конкретной книги, которой нет в наличии, и добавление одной из списка в подписки
#driver.find_element(By.CLASS_NAME, header-search__clear-icon).click()
#driver.find_element(By.TAG_NAME, input).send_keys('Терри Пратчетт Эрик')
#driver.find_element(By.XPATH, html[1]body[1]div[2]div[1]div[1]header[1]div[1]div[1]div[2]div[1]form[1]button[1][name()='svg'][1]).click()
#driver.find_element(By.CSS_SELECTOR, ) Как определить первую из списка и нажать на кнопку В подписке
                   
#sleep(5)

#3. Поиск конкретной книги и добавление в корзину
def test_buy_book(driver):
    driver.get('https://www.chitai-gorod.ru')
    driver.find_element(By.CLASS_NAME, "header-search__input").send_keys('букварь учебное пособие. надежда жукова')
    driver.find_element(By.CLASS_NAME, "header-search__button-icon").click()

    sleep(3)
    driver.find_element(By.CSS_SELECTOR, "img[alt='Букварь: Учебное пособие.']").click()
    sleep(3)
    # Ожидание загрузки элемента 
    element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[1]/div[3]/div[1]')) )
    # Скролл к элементу
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    # Клик по элементу 
    ActionChains(driver).move_to_element(element).click(element).perform()
    sleep(3)

#def test_buy_book_verify(driver):
    #driver.get('https://www.chitai-gorod.ru')
    #driver.find_element(By.CLASS_NAME, "header-search__input").send_keys('букварь учебное пособие. надежда жукова')
    #driver.find_element(By.CLASS_NAME, "header-search__button-icon").click()

    #sleep(3)
    #driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[1]/a[1]/picture[1]/img[1]").click()
    #sleep(3)
    # Ожидание загрузки элемента 
    #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[1]/div[3]/div[1]')) )
    # Скролл к элементу
    #driver.execute_script("arguments[0].scrollIntoView(true);", element)
    # Клик по элементу 
    #ActionChains(driver).move_to_element(element).click(element).perform()

    sleep(3)

#4. Поиск конкретной книги, которой нет в наличии, и добавление одной из списка в подписки