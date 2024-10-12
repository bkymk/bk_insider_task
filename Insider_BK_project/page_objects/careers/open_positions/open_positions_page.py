from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_objects.careers.careers_page import CareersPage


class OpenPositionsPage(CareersPage):
    __url = "https://useinsider.com/careers/open-positions/"
    __url_view_role = "https://jobs.lever.co/useinsider"
    __filter_menu = (By.ID, "filter-menu")
    __location_filter = (By.ID, "select2-filter-by-location-container")
    __department_filter = (By.ID, "select2-filter-by-department-container")
    __location_list = (By.ID, "select2-filter-by-location-results")
    __department_list = (By.ID, "select2-filter-by-department-results")
    __combo_box_list = (By.CLASS_NAME, "select2-results__options")
    __combo_box_option = (By.XPATH, ".//*[@class='select2-results__option' and text()='{}']")
    __job_list_loc = (By.ID, "jobs-list")

    expected_locations_set = {'All', 'Istanbul, Turkey', 'Sydney, Australia', 'Bogota, Colombia', 'Paris, France',
                              'Mexico City, Mexico', 'Bangkok, Thailand', 'London, United Kingdom',
                              'Ho Chi Minh City, Vietnam', 'Jakarta, Indonesia', 'Sao Paulo, Brazil', 'Chile, Chile',
                              'Seoul, South Korea', 'United States', 'Argentina, Argentina', 'Berlin, Germany',
                              'Kuala Lumpur, Malaysia', 'Taipei, Taiwan', 'Hanoi, Vietnam', 'Turkey', 'India, India',
                              'Warsaw, Poland'}

    expected_department_set = {'All', 'Business Development', 'Business Intelligence', 'Customer Education',
                               'Customer Success', 'Finance & Business Support', 'Human Resources',
                               'Marketing and Communications', 'Marketing Design', 'MindBehind', 'Mobile Development',
                               'Product Management', 'Sales', 'Sales Operations', 'Security', 'Software Development',
                               'Quality Assurance'}

    def __int__(self, driver: WebDriver):
        self.driver = driver

    def open_o_positions_page(self):
        self._open_url(self.__url)

    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def view_role_url(self) -> str:
        return self.__url_view_role

    def click_filter_combo(self, combo_name):
        filter_menu_element = self.driver.find_element(*self.__filter_menu)
        if combo_name == 'Location':
            combo_element = filter_menu_element.find_element(*self.__location_filter)
        # elif combo_name == 'Department':
        else:
            combo_element = filter_menu_element.find_element(*self.__department_filter)
        combo_element.click()

    def getting_location_actual_combo_set(self):
        WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.__location_list))
        list_element = self.driver.find_element(*self.__location_list)
        return set(list_element.text.split("\n"))

    def getting_department_actual_combo_set(self):
        WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.__department_list))
        list_element = self.driver.find_element(*self.__department_list)
        return set(list_element.text.split("\n"))

    def selecting_combo_list_option(self, option):
        locator = (By.XPATH, f".//*[@class='select2-results__option' and text()='{option}']")
        self.driver.find_element(*locator).click()
        WebDriverWait(self.driver, 5).until(
            ec.invisibility_of_element_located(self.__location_list))

    def wait_until_qa_department_op(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.text_to_be_present_in_element_attribute(self.__department_filter, "title", "Quality Assurance"))

    def getting_listed_jobs(self):
        WebDriverWait(self.driver, 5).until(
            ec.presence_of_element_located(self.__job_list_loc))
        job_list_element = self.driver.find_element(*self.__job_list_loc)
        listed_jobs_elements = job_list_element.find_elements(By.CLASS_NAME, "position-list-item")
        listed_jobs = []
        for b, job in enumerate(listed_jobs_elements):
            a = job.text.split("\n")
            job_map = {
                "Position": f"{a[0]}",
                "Department": f"{a[1]}",
                "Location": f"{a[2]}"}
            listed_jobs.append(job_map)
        return listed_jobs

    def checking_the_jobs_list_correct_according_to_filters_and_position_title(self, position_title_include):
        listed_jobs = self.getting_listed_jobs()
        filtered_location = self.driver.find_element(By.ID, "select2-filter-by-location-container").text.split("\n")[-1]
        filtered_department = \
            self.driver.find_element(By.ID, "select2-filter-by-department-container").text.split("\n")[-1]
        job_check_list = []
        job_check_list_map = []
        for i, element in enumerate(listed_jobs):
            if f"{filtered_department}" in listed_jobs[i]["Department"]:
                job_check_list.append(True)
            else:
                if filtered_department == 'All':
                    job_check_list.append(True)
                else:
                    job_check_list.append(False), print(f"{i}. job Department is not correct")
            if f"{filtered_location}" in listed_jobs[i]["Location"]:
                job_check_list.append(True)
            else:
                if filtered_location == 'All':
                    job_check_list.append(True)
                else:
                    job_check_list.append(False), print(f"{i}. job Location is not correct")
            if position_title_include in listed_jobs[i]["Position"]:
                job_check_list.append(True)
            else:
                job_check_list.append(False), print(f"{i}. job Position is not correct")
            job_check_list_map.append(all(job_check_list))
            job_check_list.clear()
        # print("job_check_list_map", job_check_list_map)
        return job_check_list_map

    def hover_and_click_view_role(self):
        self.driver.execute_script("window.scrollBy(0, 600);")  # Scrolls down 500 pixels
        job_list_element = self.driver.find_element(*self.__job_list_loc)
        listed_jobs_elements = job_list_element.find_elements(By.CLASS_NAME, "position-list-item")
        first_job_element = listed_jobs_elements[0]
        actions = ActionChains(self.driver)
        actions.move_to_element(first_job_element).perform()
        view_role_element = first_job_element.find_element(By.CLASS_NAME, "btn")
        WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable(view_role_element))
        view_role_element.click()

    def switch_to_view_role(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
