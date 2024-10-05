import allure
import requests
import json
import pytest
from constants import Base_url, Token

token = Token
headers = {"authorization": f"Bearer {token}"}
url = Base_url

@pytest.mark.api
@allure.epic("Читай-город") 
@allure.severity("critical")
@allure.title("Поиск товара")
@allure.description("Поиск товара через поисковую строку")
@allure.feature("GET")
def test_search_string():
    with allure.step("Отправка запроса"):
        response = requests.get(url=url + "/api/v2/search/search-phrase-suggests?suggests%5Bpage%5D=1&suggests%5Bper-page%5D=5&phrase=букварь учебное пособие. надежда жукова&include=products%2Cauthors%2CbookCycles%2CpublisherSeries%2Cpublishers%2Ccategories", headers=headers)
    with allure.step("Проверка резульата"):
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"

@pytest.mark.api
@allure.epic("Читай-город") 
@allure.severity("critical")
@allure.title("Поиск товара")
@allure.description("Поиск акций")
@allure.feature("GET")     
def test_sale_categories():
    with allure.step("Отправка запроса"):
        response = requests.get(url=url + "/api/v1/promotions?page=1&perPage=60", headers=headers)
        body = response.json()
    with allure.step("Проверка резульата"):
        assert response.status_code == 200
        assert len(body) > 0

@pytest.mark.api    
@allure.epic("Читай-город") 
@allure.severity("critical")
@allure.title("Поиск товара")
@allure.description("Поиск товара через каталог")
@allure.feature("GET")     
def test_search_catalog():
    with allure.step("Отправка запроса"):
        response = requests.get(url=url+ "/api/v1/products/slug/derzhatel-kotik-6sm-plastik-12-9412-cat-2878985", headers=headers)
    with allure.step("Проверка резульата"):
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"

@pytest.mark.api
@allure.epic("Читай-город") 
@allure.severity("critical")
@allure.title("Поиск товара")
@allure.description("Поиск товаров с наименованием из спецсимволов")
@allure.feature("GET")     
def test_negative_search_string():
    with allure.step("Отправка запроса"):
        response = requests.get(url=url + "/api/v2/search/facet-search?customerCityId=213&phrase=!!!", headers=headers)
    with allure.step("Проверка резульата"):
        assert response.status_code == 422
        assert response.is_redirect == False

@pytest.mark.api
@allure.epic("Читай-город") 
@allure.severity("critical")
@allure.title("Поиск товара")
@allure.description("Поиск товара с использованием другого метода")
@allure.feature("GET")     
def test_negative_search_POST():
    with allure.step("Отправка запроса"):
        response = requests.post(url=url+ "/api/v2/search/search-phrase-suggests?suggests%5Bpage%5D=1&suggests%5Bper-page%5D=5&phrase=букварь учебное пособие. надежда жукова&include=products%2Cauthors%2CbookCycles%2CpublisherSeries%2Cpublishers%2Ccategories", headers=headers)
    with allure.step("Проверка резульата"):
        assert response.status_code == 405
        assert response.content == b'405 method not allowed'
    