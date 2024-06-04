import datetime
import os

from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Base:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    # Locators
    locators = {
        'close_modal_inner': (By.XPATH, '//button[@class="we-closed-modal__close"]')
    }

    # Methods
    """Method to get current URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current URL: {get_url}")
        return get_url

    """Method for closing the modal window"""
    def click_close_modal(self):
        try:
            close_button = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.locators['close_modal_inner'])
            )
            close_button.click()
            print("Modal inner closed")
        except NoSuchElementException:
            print("Modal inner not found")  # Ошибка, если модальное окно не найдено
        except TimeoutException:
            print("Timed out waiting for modal to close")   # Ошибка, если время ожидания закрытия модального окна истекло
            self.take_screenshot('modal_timeout')
        except Exception as e:
            print(f"Error while closing modal: {e}")  # Общая ошибка закрытия модального окна

    """Method for clicking on the elements"""
    def click_element(self, locator_name, retries=3):
        locator = self.locators[locator_name]
        for attempt in range(retries):
            try:
                element = WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable(locator)
                )
                self.scroll_to_element_center(element)
                element.click()
                print(f"Clicked element: {locator_name}")
                return
            except StaleElementReferenceException:
                if attempt < retries - 1:
                    print(f"Retrying click for element: {locator_name}")  # Ошибка, если не удалось кликнуть по элементу
                else:
                    print(f"Failed to click element after {retries} attempts: {locator_name}")
                    self.take_screenshot('stale_element')
            except TimeoutException:
                print(f"Timed out waiting for element: {locator_name}")  # Ошибка, если время ожидания элемента истекло
                self.take_screenshot('timeout')
                raise
            except ElementClickInterceptedException:
                if attempt < retries - 1:
                    print(f"Element click intercepted, retrying: {locator_name}")  # Предупреждение о перехваченном клике
                    self.handle_intercepted_click(locator)
                else:
                    print(f"Failed to click element after {retries} attempts: {locator_name}")  # Ошибка, если не удалосm кликнуть по элементу
                    self.take_screenshot('intercepted_element')
                    raise
            except Exception as e:
                print(f"Error clicking element: {locator_name} - {e}")  # Общая ошибка клика по элементу
                self.take_screenshot('exception')
                raise

    """where another element is intercepting the click"""
    def handle_intercepted_click(self, locator):
        try:
            WebDriverWait(self.driver, 5).until_not(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".catalog-content__prods-bg.show"))
            )
            element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(locator)
            )
            self.scroll_to_element(element)  # Убедимся, что элемент доступен
            element.click()
        except Exception as e:
            print(f"Error handling intercepted click: {e}")
            self.take_screenshot('handle_intercepted_click')
            raise

    """Method to scroll to an element"""

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        print("Scrolled to element")

    """Method to scroll to an element center"""
    def scroll_to_element_center(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
        print("Scrolled to element center")

    """Method screenshot"""

    def take_screenshot(self, name):
        now_date = datetime.datetime.today().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = f"{name}{now_date}.png"
        # Путь к папке screen в корне проекта
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        screenshots_dir = os.path.join(project_root, 'screen')
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        screenshot_path = os.path.join(screenshots_dir, name_screenshot)
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

    """Method assert URL"""

    def get_assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print(f"Good assertion URL: {get_url}")
