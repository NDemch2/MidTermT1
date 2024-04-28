import unittest
from selenium import webdriver
from actions import MainPage, MenCategoryPage, ProductDetailPage

class TestPurchase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://magento.softwaretestingboard.com/')
        self.main_page = MainPage(self.driver)
        self.men_category_page = MenCategoryPage(self.driver)
        self.product_detail_page = ProductDetailPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_purchase_item(self):
        
        self.main_page.go_to_men_category()

       
        self.men_category_page.choose_product()

        self.product_detail_page.select_size()
        
        self.product_detail_page.select_color()
        
        self.product_detail_page.add_to_cart()

        
        error_message = self.product_detail_page.get_error_message()
        self.assertIsNone(error_message, "Error message found: {}".format(error_message))

if __name__ == "__main__":
    unittest.main()
