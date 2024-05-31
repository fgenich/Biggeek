from selenium.webdriver.common.by import By
from base.base_class import Base

class Catalog_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators.update({
            'apple_iphone': (By.XPATH, '//div/a[contains(text(),"Смартфоны Apple iPhone")]'),
            'memory': (By.XPATH, '//span[contains(text(),"512")]'),
            'model': (By.XPATH, '//a[@href="apple-iphone-15-pro"]'),
            'color': (By.XPATH, '//span[contains(text(),"Натуральный титан")]'),
            'sort_items': (By.XPATH, '//p[@class="simple-select__selected"]'),
            'sort_price': (By.XPATH, '//li[@data-value="price"]'),
            'open_product': (By.XPATH, '(//div[@class="catalog-card"])[1]'),
            'select_radio_button': (By.XPATH, '(//div[@class="i-radio"])[2]'),
            'add_to_cart': (By.XPATH, '//div[@class="prod-info-price__btns"]'),
            'go_to_cart': (By.XPATH, '//a[contains(text(),"Перейти")]')
        })

    # Actions
    def click_apple_iphone(self):
        self.click_element('apple_iphone')

    def click_memory(self):
        self.click_element('memory')

    def click_model(self):
        self.click_element('model')

    def click_color(self):
        self.click_element('color')

    def click_sort_items(self):
        self.click_element('sort_items')

    def click_sort_price(self):
        self.click_element('sort_price')

    def click_open_product(self):
        self.click_element('open_product')

    # Methods
    def select_product(self):
        self.get_current_url()
        self.get_assert_url('https://biggeek.ru/catalog/apple')
        self.click_close_modal()
        self.click_apple_iphone()
        self.click_model()
        self.click_memory()
        self.click_color()
        self.click_sort_items()
        self.click_sort_price()
        self.click_open_product()
        print('Product selected')

