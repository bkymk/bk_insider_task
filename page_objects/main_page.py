from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class MainPage(BasePage):
    URL = "https://useinsider.com/"
    NAVBAR = (By.ID, "navbarNavDropdown")
    NAVBAR_DROPDOWNS = (By.CLASS_NAME, "navbar-nav")
    NAVBAR_OPTIONS = (By.XPATH, ".//*[@class='nav-item dropdown']")
    POP_UP_CLOSE_BUTTON = (By.CLASS_NAME, "ins-close-button")
    DROPDOWN_SUB = (By.CLASS_NAME, "dropdown-sub")
    PRESENTED_NAV_BAR_ITEM = (By.XPATH, ".//*[@class='nav-item dropdown show']")
    EXPECTED_NAV_BAR_SET = {"Why Insider", "Platform", "Solutions", "Customers", "Resources", "Company"}
    EXPECTED_COMPANY_TAB_SET = {"About Us", "Newsroom", "Partnerships", "Integrations", "Careers", "Contact Us"}

    def __int__(self, driver: WebDriver):
        self.driver = driver

    def open_main_page(self):
        self.open_url(self.URL)

    @property
    def expected_url(self) -> str:
        return self.URL

    @property
    def expected_nav_bar_set(self) -> set:
        return self.EXPECTED_NAV_BAR_SET

    @property
    def expected_company_dropdown_menu_set(self) -> set:
        return self.EXPECTED_COMPANY_TAB_SET

    def getting_nav_bar_text_and_clicking_option(self, option: str | None = None) -> set:
        nav_bar_element = self.driver.find_element(*self.NAVBAR_DROPDOWNS)
        nav_bar_all_elements = nav_bar_element.find_elements(*self.NAVBAR_OPTIONS)
        nav_bar_set = set()
        # Last element of navbar changing every run son last one is discarded
        for each_element in nav_bar_all_elements[:-1]:
            nav_bar_set.add(each_element.text)
            if option is not None and each_element.text == option:
                each_element.click()
                break
        else:
            return nav_bar_set

    def getting_dropdown_menu_and_clicking_option(self, option: str | None = None) -> set:
        dropdown_sub_elements = self.driver.find_element(*self.PRESENTED_NAV_BAR_ITEM).find_elements(
            *self.DROPDOWN_SUB)
        presented_dropdown_menu_set = set()
        for dropdown_sub_element in dropdown_sub_elements:
            presented_dropdown_menu_set.add(dropdown_sub_element.text)
            if option is not None and dropdown_sub_element.text == option:
                dropdown_sub_element.click()
                break
        else:
            return presented_dropdown_menu_set
