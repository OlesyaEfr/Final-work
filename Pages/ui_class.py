import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
   
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.chitai-gorod.ru/"

    @allure.step("Перейти на сайт") 
    def go_to_site(self):
        return self.driver.get(self.base_url)
