import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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
    def enter_text(self, locator_name, text):  # Ввод текста с использованием явного ожидания
        try:
            locator = self.locators[locator_name]
            element = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(locator)
            )
            element.clear()
            element.send_keys(text)
            print(f"Entered text '{text}' into element: {locator_name}")
        except Exception as e:
            print(f"Error while entering text into element {locator_name}: {e}")
            self.take_screenshot(f'enter_text_error_{locator_name}')
            raise

    def click_checkbox_1(self):  # Клик на чекбокс
        self.click_element('checkbox_1')

    def click_confirm_button(self):  # Клик на кнопку подверждения
        self.click_element('confirm_button')

    def confirmation(self):
        """Method of confirmation order"""
        with allure.step('Confirm order'):
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

