from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pytest
from pages.sale import Sale
from pages.eco_friendly import EcoFriendlySorting
from pages.create_account import AccountCreation


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920x1080')
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    chrome_driver = webdriver.Chrome()
    return chrome_driver


@pytest.fixture()
def sale_page(driver):
    return Sale(driver)


@pytest.fixture()
def login_page(driver):
    return AccountCreation(driver)


@pytest.fixture()
def ecofriendly_page(driver):
    return EcoFriendlySorting(driver)
