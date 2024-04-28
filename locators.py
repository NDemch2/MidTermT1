from selenium.webdriver.common.by import By

class MainPageLocators:
    MEN_CATEGORY_LINK = (By.XPATH, "//*[@id='ui-id-5']")

class MenCategoryPageLocators:
    PRODUCT_LIST = (By.XPATH, "//*[@id='maincontent']/div[4]/div[1]/div[2]/div[3]/div/div/ol/li[2]/div/a/span/span/img")

class ProductDetailPageLocators:
    ADD_TO_CART_BUTTON = (By.ID, "product-addtocart-button")
    SIZE_OPTION = (By.XPATH, "//*[@id='option-label-size-143-item-166']")
    COLOR_OPTION = (By.XPATH, "//*[@id='product-addtocart-button']")

