from selenium.webdriver.common.by import By

class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

        self.add_to_cart = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart).click()

    def open_cart(self):
        self.driver.find_element(*self.cart_button).click()