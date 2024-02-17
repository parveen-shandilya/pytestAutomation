# For Fixture 

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(params=['chrome'],scope='class')
def init_driver(request):
    if request.param == 'chrome':
        chrome_option = Options()
        chrome_option.add_experimental_option("detach",True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_option)
   
    
    request.cls.driver = driver
    yield
    driver.quit()
    