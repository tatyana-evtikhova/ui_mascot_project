from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class EcoFriendlySorting(BasePage):
    page_url = '/collections/eco-friendly.html'

    def sort_items_by_name_descending(self):
        sorter = self.driver.find_element(By.ID, 'sorter')
        select = Select(sorter)
        select.select_by_value('name')
        self.driver.find_element(By.CSS_SELECTOR, 'a.action.sorter-action[data-value="desc"]').click()

    def check_first_item_after_sorting_descending(self):
        items = self.driver.find_elements(By.CLASS_NAME, 'product-item-link')
        first_item = items[0]
        assert first_item.text == 'Tiffany Fitness Tee'

    def sort_items_by_price(self):
        sorter = self.driver.find_element(By.ID, 'sorter')
        select = Select(sorter)
        select.select_by_value('price')

    def check_first_item_after_sorting(self):
        items = self.driver.find_elements(By.CLASS_NAME, 'product-item-link')
        first_item = items[0]
        assert first_item.text == 'Atlas Fitness Tank'

    def check_initial_toolbar_text(self):
        toolbar_text = self.driver.find_element(By.ID, 'toolbar-amount').text
        assert toolbar_text == "Items 1-12 of 18"

    def switch_to_list_view(self):
        list_view_button = self.driver.find_element(By.ID, 'mode-list').click()

    def check_updated_toolbar_text(self):
        toolbar_text = self.driver.find_element(By.ID, 'toolbar-amount').text
        assert toolbar_text == "Items 1-10 of 18"
