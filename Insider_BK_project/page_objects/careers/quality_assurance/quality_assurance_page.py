from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class QualityAssurancePage(BasePage):
    __url = "https://useinsider.com/careers/quality-assurance/"
    __button_row = (By.XPATH, ".//*[@class='button-group d-flex flex-row']")
    __see_all_qa_jobs_button = (By.CLASS_NAME, "btn")

    def __int__(self, driver: WebDriver):
        self.driver = driver

    def open_qa_page(self):
        self._open_url(self.__url)

    @property
    def expected_url(self) -> str:
        return self.__url

    def click_see_all_qa_job_button(self):
        button_row_element = self.driver.find_element(*self.__button_row)
        see_all_qa_jobs_element = button_row_element.find_element(*self.__see_all_qa_jobs_button)
        see_all_qa_jobs_element.click()
