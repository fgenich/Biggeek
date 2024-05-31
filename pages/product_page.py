from selenium.webdriver.common.by import By
from base.base_class import Base

class Product_page(Base):
    url = 'https://biggeek.ru/products/apple-iphone-15-pro-512gb-naturalnyj-titan-natural-titanium'
    def __init__(self, driver):
        super().__init__(driver)
        self.locators.update({
            'select_radio_button': (By.XPATH, '(//div[@class="i-radio"])[2]'),
            'add_to_cart': (By.XPATH, '//div[@class="prod-info-price__btns"]'),
            'go_to_cart': (By.XPATH, '//a[contains(text(),"Перейти")]')
        })

    # Actions
    def click_radio_button(self):
        self.click_element('select_radio_button')

    def click_add_to_cart(self):
        self.click_element('add_to_cart')

    def click_go_to_cart(self):
        self.click_element('go_to_cart')

    # Methods
    def add_product_to_cart(self):
        self.get_current_url()
        self.get_assert_url(self.url)
        self.click_close_modal()
        self.click_radio_button()
        self.click_add_to_cart()
        self.click_go_to_cart()
        print('Product added to cart')
