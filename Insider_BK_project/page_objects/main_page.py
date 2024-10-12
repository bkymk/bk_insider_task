from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class MainPage(BasePage):
    __url = "https://useinsider.com/"
    __navbar = (By.ID, "navbarNavDropdown")
    __navbar_dropdowns = (By.CLASS_NAME, "navbar-nav")
    __navbar_options = (By.XPATH, ".//*[@class='nav-item dropdown']")
    __pop_up_close_button = (By.CLASS_NAME, "ins-close-button")
    __dropdown_sub = (By.CLASS_NAME, "dropdown-sub")
    __presented_nav_bar_item = (By.XPATH, ".//*[@class='nav-item dropdown show']")
    __expected_nav_bar_set = {"Why Insider", "Platform", "Solutions", "Customers", "Resources", "Company"}
    __expected_company_tab_set = {"About Us", "Newsroom", "Partnerships", "Integrations", "Careers", "Contact Us"}

    def __int__(self, driver: WebDriver):
        self.driver = driver

    def open_main_page(self):
        self._open_url(self.__url)

    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def expected_nav_bar_set(self) -> set:
        return self.__expected_nav_bar_set

    @property
    def expected_company_dropdown_menu_set(self) -> set:
        return self.__expected_company_tab_set

    def getting_nav_bar_text_and_clicking_option(self, option: str) -> set:
        nav_bar_element = self.driver.find_element(*self.__navbar_dropdowns)
        nav_bar_all_elements = nav_bar_element.find_elements(*self.__navbar_options)
        nav_bar_all_elements.pop(-1)
        nav_bar_set = set()
        target = None
        for i, each_element in enumerate(nav_bar_all_elements):
            nav_bar_set.add(each_element.text)
            if nav_bar_all_elements[i].text == option:
                target = i
        nav_bar_all_elements[target].click()
        return nav_bar_set

    def getting_dropdown_menu_and_clicking_option(self, option: str) -> set:
        dropdown_sub_elements = self.driver.find_element(*self.__presented_nav_bar_item).find_elements(
            *self.__dropdown_sub)
        presented_dropdown_menu_set = set()
        target = None
        for i, dropdown_sub_element in enumerate(dropdown_sub_elements):
            presented_dropdown_menu_set.add(dropdown_sub_element.text)
            if dropdown_sub_elements[i].text == option:
                target = i
        dropdown_sub_elements[target].click()
        return presented_dropdown_menu_set
