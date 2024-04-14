from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import random
import string


class AccountCreation(BasePage):
    page_url = '/customer/account/create/'

    def fill_registration_form(self, firstname, lastname, password, confirmation_password):
        email = self.generate_random_email()
        firstname_field = self.driver.find_element(By.ID, "firstname").send_keys(firstname)
        lastname_field = self.driver.find_element(By.ID, "lastname").send_keys(lastname)
        email_field = self.driver.find_element(By.ID, "email_address").send_keys(email)
        password_field = self.driver.find_element(By.ID, "password").send_keys(password)
        confirmation_password_field = self.driver.find_element(By.ID, "password-confirmation").send_keys(
            confirmation_password)
        button = self.driver.find_element(By.CSS_SELECTOR, ".action.submit.primary").click()

    def generate_random_email(self):
        random_string = ''.join(random.choices(string.ascii_lowercase, k=8))
        return f"{random_string}@example.com"

    def check_successful_registration(self):
        message_element = self.driver.find_element(By.XPATH, '//div[contains(text(), "Thank you for registering with '
                                                             'Main Website Store.")]')
        assert message_element.text == 'Thank you for registering with Main Website Store.'

    def check_guest_message(self):
        message_element = self.driver.find_element(By.XPATH, '//span[@class="not-logged-in"]')
        assert message_element.text == 'Click “Write for us” link in the footer to submit a guest post'

    def invalid_email(self):
        email_input = self.driver.find_element(By.ID, "email_address").send_keys('invalid email')
        submit_button = self.driver.find_element(By.CSS_SELECTOR, '[title="Create an Account"]').click()

    def check_email_validation(self):
        error_message = self.driver.find_element(By.ID, 'email_address-error').text
        expected_message = 'Please enter a valid email address (Ex: johndoe@domain.com).'
        assert error_message == expected_message