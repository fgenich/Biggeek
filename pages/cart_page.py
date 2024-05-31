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

    """Method of enter the text"""
    def enter_text(self, locator_name, text):
        try:
            element = self.driver.find_element(*self.locators[locator_name])
            element.clear()
            element.send_keys(text)
            print(f"Entered text '{text}' into element: {locator_name}")
        except Exception as e:
            print(f"Error while entering text into element {locator_name}: {e}")
            self.take_screenshot(f'enter_text_error_{locator_name}')
            raise

    """Method of click the checkbox"""
    def click_checkbox_1(self):
        self.click_element('checkbox_1')

    """Method of click the confirm button"""
    def click_confirm_button(self):
        self.click_element('confirm_button')

    """Method of confirmation order"""
    def confirmation(self):
        try:
            self.click_close_modal()
            self.get_current_url()
            self.get_assert_url('https://biggeek.ru/cart')
            self.enter_text('name', 'John')  # Введите имя
            self.enter_text('last_name', 'Doe')  # Введите фамилию
            self.enter_text('email', 'john.doe@example.com')  # Введите email
            self.enter_text('phone', '1234567890')  # Введите номер телефона
            self.enter_text('comment', 'This is a test comment.')  # Введите комментарий
            self.click_checkbox_1()
            self.click_confirm_button()
            print('Confirmation success')
        except Exception as e:
            print(f"Error during confirmation: {e}")
            self.take_screenshot('confirmation_error')
            raise

