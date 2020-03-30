from .base_page import BasePage
from .locators import ProductPageLocators
import math
import time
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):

    def add_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_link.click()


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(20000)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_name_of_product(self):
        product_name_link = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT)
        assert "Coders at Work" == product_name_link.text, "error"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_IN_CART), \
            "Success message is presented, but should not be"

    def should_be_dissapered_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_PRODUCT_IN_CART), \
            "Success message is dissapered, but should not be"





