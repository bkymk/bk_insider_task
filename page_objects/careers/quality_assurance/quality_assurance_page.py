from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


# Quality Assurance page is reached from teams blocks
class QualityAssurancePage(BasePage):
    URL = "https://useinsider.com/careers/quality-assurance/"
    BUTTON_ROW = (By.XPATH, ".//*[@class='button-group d-flex flex-row']")
    SEE_ALL_QA_JOBS_BUTTON = (By.CLASS_NAME, "btn")

    def __int__(self, driver: WebDriver):
        self.driver = driver

    def open_qa_page(self):
        self.open_url(self.URL)

    @property
    def expected_url(self) -> str:
        return self.URL

    def click_see_all_qa_job_button(self):
        button_row_element = self.driver.find_element(*self.BUTTON_ROW)
        see_all_qa_jobs_element = button_row_element.find_element(*self.SEE_ALL_QA_JOBS_BUTTON)
        see_all_qa_jobs_element.click()
