import pytest
from selenium import webdriver
from pages.main_page import Main_page
from pages.catalog_page import Catalog_page
from pages.product_page import Product_page
from pages.cart_page import Cart_page

def test_buy_product():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    print('Start test')

    mp = Main_page(driver)
    mp.get_all_apples()

    cp = Catalog_page(driver)
    cp.select_product()

    pp = Product_page(driver)
    pp.add_product_to_cart()

    cart_p = Cart_page(driver)
    cart_p.confirmation()

    print('End test')


