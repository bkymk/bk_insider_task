from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def current_url(self) -> str:
        return self.driver.current_url

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self.driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False

    def _open_url(self, url: str):
        self.driver.get(url)

    def is_displayed(self, locator: tuple) -> bool:
        try:
            return self.driver.find_element(locator).is_displayed()
        except NoSuchElementException:
            return False

    def is_url_correct(self, url):
        try:
            WebDriverWait(self.driver, 5).until(
                ec.url_contains(url))
            return True
        except:
            return False
