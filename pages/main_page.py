from selenium.webdriver.common.by import By
from base.base_class import Base

class Main_page(Base):
    url = 'https://biggeek.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.locators.update({
            'all_items': (By.XPATH, '//button[@class="dropdown-header__button"]'),
            'all_apple': (By.XPATH, '//a[@href="/catalog/apple"]')
        })

    # Actions
    def move_to_all_items(self):
        self.click_element('all_items')

    def click_all_apple(self):
        self.click_element('all_apple')

    # Methods
    def get_all_apples(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.get_assert_url(self.url)
        self.click_close_modal()
        self.move_to_all_items()
        self.click_all_apple()

