import requests
import json
import pytest

BaseURL = "https://web-gate.chitai-gorod.ru"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIwMTA0MDc1LCJpYXQiOjE3Mjc3MDY0NTcsImV4cCI6MTcyNzcxMDA1NywidHlwZSI6MjB9.VC2AR4H6R5J2U9flUGaM6u7jY7KyQnxNfquSAcK9xMM"
headers = {"authorization": f"Bearer {token}"}

#1.Поиск товара через поисковую строку
def test_search_string():
    response = requests.get(BaseURL + "/api/v2/search/search-phrase-suggests?suggests%5Bpage%5D=1&suggests%5Bper-page%5D=5&phrase=букварь учебное пособие. надежда жукова&include=products%2Cauthors%2CbookCycles%2CpublisherSeries%2Cpublishers%2Ccategories", headers=headers)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
     
#2.Поиск акций
def test_sale_categories():
    response = requests.get(BaseURL + "/api/v1/promotions?page=1&perPage=60", headers=headers)
    body = response.json()
    assert response.status_code == 200
    assert len(body) > 0
    

#3.Поиск товара через каталог
def test_search_catalog():
    response = requests.get(BaseURL + "/api/v1/products/slug/derzhatel-kotik-6sm-plastik-12-9412-cat-2878985", headers=headers)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

#4.Поиск товаров с наименованием из спецсимволов
def test_negative_search_string():
    response = requests.get(BaseURL + "/api/v2/search/facet-search?customerCityId=213&phrase=!!!", headers=headers)
    assert response.status_code == 422
    assert response.is_redirect == False

#5.Поиск товара с использованием другого метода
def test_negative_search_POST():
    response = requests.post(BaseURL + "/api/v2/search/search-phrase-suggests?suggests%5Bpage%5D=1&suggests%5Bper-page%5D=5&phrase=букварь учебное пособие. надежда жукова&include=products%2Cauthors%2CbookCycles%2CpublisherSeries%2Cpublishers%2Ccategories", headers=headers)
    assert response.status_code == 405
    assert response.content == b'405 method not allowed'
    