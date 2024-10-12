from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class CareersPage(BasePage):
    __url = "https://useinsider.com/careers/"
    __locations_block = (By.CSS_SELECTOR, '[data-id="38b8000"]')
    __teams_block = (By.CSS_SELECTOR, '[data-id="b0965d6"]')
    __life_at_insider_block = (By.CSS_SELECTOR, '[data-id="a8e7b90"]')

    def __int__(self, driver: WebDriver):
        self.driver = driver

    def open_careers_page(self):
        self._open_url(self.__url)

    @property
    def expected_url(self) -> str:
        return self.__url

    def is_locations_blocks_displayed(self) -> bool:
        return self._is_displayed(self.__locations_block)

    def is_teams_blocks_displayed(self) -> bool:
        return self._is_displayed(self.__teams_block)

    def is_life_blocks_displayed(self) -> bool:
        return self._is_displayed(self.__life_at_insider_block)
