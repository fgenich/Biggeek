from selenium.webdriver.common.by import By
from base.base_class import Base

class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators.update({
            'name': (By.XPATH, '(//input[@name="name"])[1]'),
            'last_name': (By.XPATH, '//input[@name="last_name"]'),
            'email': (By.XPATH, '(//input[@id="email"])[1]'),
            'phone': (By.XPATH, '(//input[@id="phone"])[1]'),
            'comment': (By.XPATH, '//textarea[@name="comment"]'),
            'checkbox_1': (By.XPATH, '//label[@for="step-subscription"]'),
            'confirm_button': (By.XPATH, '//button[contains(text(),"Оформить")]')
        })

    # Actions
    def enter_name(self):
        self.click_element('name')

    def enter_last_name(self):
        self.click_element('last_name')

    def enter_email(self):
        self.click_element('email')

    def enter_phone(self):
        self.click_element('phone')

    def enter_comment(self):
        self.click_element('comment')

    def click_checkbox_1(self):
        self.click_element('checkbox_1')

    def click_confirm_button(self):
        self.click_element('confirm_button')

    # Methods
    def confirmation(self):
        try:
            self.click_close_modal()
            self.get_current_url()
            self.get_assert_url('https://biggeek.ru/cart')
            self.enter_name()
            self.enter_last_name()
            self.enter_email()
            self.enter_phone()
            self.enter_comment()
            self.click_checkbox_1()
            self.click_confirm_button()
            print('Confirmation success')
        except Exception as e:
            print(f"Error during confirmation: {e}")
            self.take_screenshot('confirmation_error')
            raise
