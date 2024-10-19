from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


# Careers page is reached from Company dropdown which is on navbar
class CareersPage(BasePage):
    URL = "https://useinsider.com/careers/"
    LOCATIONS_BLOCK = (By.CSS_SELECTOR, '[data-id="38b8000"]')
    TEAMS_BLOCK = (By.CSS_SELECTOR, '[data-id="b0965d6"]')
    LIFE_AT_INSIDER_BLOCK = (By.CSS_SELECTOR, '[data-id="a8e7b90"]')

    def __int__(self, driver: WebDriver):
        self.driver = driver

    @property
    def expected_url(self) -> str:
        return self.URL

    def is_locations_blocks_displayed(self) -> bool:
        return self.is_displayed(self.LOCATIONS_BLOCK)

    def is_teams_blocks_displayed(self) -> bool:
        return self.is_displayed(self.TEAMS_BLOCK)

    def is_life_blocks_displayed(self) -> bool:
        return self.is_displayed(self.LIFE_AT_INSIDER_BLOCK)
