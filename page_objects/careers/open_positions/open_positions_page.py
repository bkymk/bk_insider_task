import time
import random
from typing import Literal

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.careers.careers_page import CareersPage


# Open Positions page is reached from Quality Assurance page also it can be reached from "Find your dream job" button on Careers Page
class OpenPositionsPage(CareersPage):
    URL = "https://useinsider.com/careers/open-positions/"
    URL_VIEW_ROLE = "https://jobs.lever.co/useinsider"
    FILTER_MENU = (By.ID, "filter-menu")
    FILTER_DROPDOWM = "select2-filter-by-{}-container"
    DEPARTMENT_FILTER = (By.ID, "select2-filter-by-department-container")
    LOCATION_LIST = (By.ID, "select2-filter-by-location-results")
    DEPARTMENT_LIST = (By.ID, "select2-filter-by-department-results")
    COMBO_BOX_LIST = (By.CLASS_NAME, "select2-results__options")
    COMBO_BOX_OPTION = (By.XPATH, ".//*[@class='select2-results__option' and text()='{}']")
    JOB_LIST_LOC = (By.ID, "jobs-list")

    EXPECTED_LOCATIONS_SET = {'All', 'Istanbul, Turkey', 'Sydney, Australia', 'Bogota, Colombia', 'Paris, France',
                              'Mexico City, Mexico', 'Bangkok, Thailand', 'London, United Kingdom',
                              'Ho Chi Minh City, Vietnam', 'Jakarta, Indonesia', 'Sao Paulo, Brazil', 'Chile, Chile',
                              'Seoul, South Korea', 'United States', 'Argentina, Argentina', 'Berlin, Germany',
                              'Kuala Lumpur, Malaysia', 'Taipei, Taiwan', 'Hanoi, Vietnam', 'Turkey', 'India, India',
                              'Warsaw, Poland'}

    EXPECTED_DEPARTMENT_SET = {'All', 'Business Development', 'Business Intelligence', 'Customer Education',
                               'Customer Success', 'Finance & Business Support', 'Human Resources',
                               'Marketing and Communications', 'Marketing Design', 'MindBehind', 'Mobile Development',
                               'Product Management', 'Sales', 'Sales Operations', 'Security', 'Software Development',
                               'Quality Assurance'}

    def __int__(self, driver: WebDriver):
        self.driver = driver

    @property
    def expected_url(self) -> str:
        return self.URL

    @property
    def view_role_url(self) -> str:
        return self.URL_VIEW_ROLE

    def click_filter_combo(self, combo_name: Literal["department", "location"]):
        # Formating Filter Dropdown locator from combo name which is location or department
        locator = self.FILTER_DROPDOWM.format(combo_name)
        self.driver.find_element(By.ID, locator).click()

    def getting_location_actual_combo_set(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.LOCATION_LIST))
        list_element = self.driver.find_element(*self.LOCATION_LIST)
        return set(list_element.text.split("\n"))

    def getting_department_actual_combo_set(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.DEPARTMENT_LIST))
        list_element = self.driver.find_element(*self.DEPARTMENT_LIST)
        return set(list_element.text.split("\n"))

    def selecting_combo_list_option(self, option):
        locator = (By.XPATH, f".//*[@class='select2-results__option' and text()='{option}']")
        self.driver.find_element(*locator).click()
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(self.LOCATION_LIST))

    def wait_until_qa_department_op(self):
        # Since reaching open positions page from Quality Assurance, should be waiting department filter to be presented as Quality Assurance
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.text_to_be_present_in_element_attribute(self.DEPARTMENT_FILTER, "title", "Quality Assurance"))

    def wait_until_reload(self):
        # Waiting for DOM the refresh
        a = time.time()
        WebDriverWait(self.driver, timeout=10).until(lambda x: self.page_has_loaded())
        print("Reload Time", time.time() - a)

    def are_listed_jobs_correct(self):
        job_list_element = self.driver.find_element(*self.JOB_LIST_LOC)
        listed_jobs_elements = job_list_element.find_elements(By.CLASS_NAME, "position-list-item")
        for job in listed_jobs_elements:
            position, department, location = job.text.split("\n")
            if ('Quality Assurance' not in position) or (
                    (department, location) != ('Quality Assurance', 'Istanbul, Turkey')):
                print("position,department, location", position, department, location)
                return False
        return True

    def hover_and_click_view_role(self):
        self.driver.execute_script("window.scrollBy(0, 300);")  # Scrolls down 500 pixels
        job_list_element = self.driver.find_element(*self.JOB_LIST_LOC)
        listed_jobs_elements = job_list_element.find_elements(By.CLASS_NAME, "position-list-item")
        # Selecting one of the listed jobs randomly
        job_element = random.choice(listed_jobs_elements)
        actions = ActionChains(self.driver)
        actions.move_to_element(job_element).perform()
        view_role_element = job_element.find_element(By.CLASS_NAME, "btn")
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(view_role_element))
        view_role_element.click()

    def switch_to_view_role(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
