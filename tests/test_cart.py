from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart():

    driver = get_driver()

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open()

    login.login(
        "standard_user",
        "secret_sauce"
    )

    inventory.add_product_to_cart()
    inventory.open_cart()

    assert "cart" in driver.current_url

    driver.quit()