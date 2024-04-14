from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
            consent_button = self.driver.find_element(By.CSS_SELECTOR, 'p.fc-button-label').click()
        else:
            raise NotImplementedError('Page can not be opened for this page class')