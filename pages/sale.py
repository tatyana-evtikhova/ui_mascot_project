from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Sale(BasePage):
    page_url = '/sale.html'

    def check_20_percent_promo(self):
        promo_element = self.driver.find_element(By.CSS_SELECTOR, "a.block-promo.sale-20-off")
        assert promo_element.find_element(By.CSS_SELECTOR, "strong.title").text == "20% OFF"
        assert promo_element.find_element(By.CSS_SELECTOR, "span.info").text == "Every $200-plus purchase!"

    def woman_deals_redirect(self):
        women_deals_link = self.driver.find_element(By.CSS_SELECTOR, "a.block-promo.sale-main").click()

    def check_redirection_to_woman_deals(self):
        expected_url = "https://magento.softwaretestingboard.com/promotions/women-sale.html"
        current_url = self.driver.current_url
        assert expected_url == current_url

    def header_text_is(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'h1.page-title#page-title-heading').text

    def check_header_text(self, expected_text):
        actual_text = self.header_text_is()
        assert expected_text == actual_text