import pytest
import allure
from selenium import webdriver
from pages.main_page import Main_page
from pages.catalog_page import Catalog_page
from pages.product_page import Product_page
from pages.cart_page import Cart_page


def test_buy_product():
    """Поиск нужного товара с помощью фтльтра по котологу и его оформление"""
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    print('Start test')

    mp = Main_page(driver)
    mp.get_all_apples()  # Переход в каталог со всеми товарами Apple

    cp = Catalog_page(driver)
    cp.select_product()  # Выбор критерий фильтра и переход на нужный товар

    pp = Product_page(driver)
    pp.add_product_to_cart()  # Добавление товара в каризну

    cart_p = Cart_page(driver)
    cart_p.confirmation()  # Подтверждение покупки

    print('End test')


