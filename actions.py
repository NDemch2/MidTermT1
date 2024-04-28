from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, MenCategoryPageLocators, ProductDetailPageLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_men_category(self):
        men_category_link = self.driver.find_element(*MainPageLocators.MEN_CATEGORY_LINK)
        men_category_link.click()

class MenCategoryPage:
    def __init__(self, driver):
        self.driver = driver

    def choose_product(self):
        product_list = self.driver.find_elements(*MenCategoryPageLocators.PRODUCT_LIST)
        product_list[0].click()

class ProductDetailPage:
    def __init__(self, driver):
        self.driver = driver
    
    def select_size(self):
        size_option = self.driver.find_element(*ProductDetailPageLocators.SIZE_OPTION)
        size_option.click()

    def select_color(self):
        color_option = self.driver.find_element(*ProductDetailPageLocators.COLOR_OPTION)
        color_option.click()


    def add_to_cart(self):
        add_to_cart_button = self.driver.find_element(*ProductDetailPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def get_error_message(self):
        try:
            error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ProductDetailPageLocators.ERROR_MESSAGE))
            return error_message.text
        except:
            return None
