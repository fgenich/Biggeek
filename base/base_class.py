import datetime

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

    """Method to get current URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current URL: {get_url}")
        return get_url


    # Locators
    locators = {
        'close_modal_inner': (By.XPATH, '//button[@class="we-closed-modal__close"]')
    }

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
                    WebDriverWait(self.driver, 5).until_not(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".catalog-content__prods-bg.show"))
                    )
                else:
                    print(f"Failed to click element after {retries} attempts: {locator_name}")  # Ошибка, если не удалось кликнуть по элементу
                    self.take_screenshot('intercepted_element')
                    raise
            except Exception as e:
                print(f"Error clicking element: {locator_name} - {e}")  # Общая ошибка клика по элементу
                self.take_screenshot('exception')
                raise

    """Method screenshot"""

    def take_screenshot(self, name, directory='/Users/fgenich/PycharmProjects/Biggeek/screen/'):
        now_date = datetime.datetime.today().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = f"{name}{now_date}.png"
        self.driver.save_screenshot(f'{directory}{name_screenshot}')

    """Method assert URL"""

    def get_assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print(f"Good assertion URL: {get_url}")
