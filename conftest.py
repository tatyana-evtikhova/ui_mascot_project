from selenium import webdriver
import pytest
from pages.sale import Sale
from pages.eco_friendly import EcoFriendlySorting
from pages.create_account import AccountCreation


@pytest.fixture()
def driver():
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

