import time
import pytest

from page_objects.careers.careers_page import CareersPage
from page_objects.careers.open_positions.open_positions_page import OpenPositionsPage
from page_objects.careers.quality_assurance.quality_assurance_page import QualityAssurancePage
from page_objects.main_page import MainPage


class TestInsiderScenarios:
    @pytest.mark.testinsider
    def test_insider_job_filter(self, driver):
        main_page = MainPage(driver)
        careers_page = CareersPage(driver)
        qa_page = QualityAssurancePage(driver)
        op_page = OpenPositionsPage(driver)
        main_page.open_main_page()
        assert main_page.current_url == main_page.expected_url, "Main Page URL Not As Expected"
        assert main_page.getting_nav_bar_text_and_clicking_option() == main_page.expected_nav_bar_set, "Nav Bar Dropdown Set Not As Expected"
        main_page.getting_nav_bar_text_and_clicking_option("Company")
        assert main_page.getting_dropdown_menu_and_clicking_option() == main_page.expected_company_dropdown_menu_set, "Company Dropdown Set Not As Expected"
        main_page.getting_dropdown_menu_and_clicking_option("Careers")
        assert careers_page.current_url == careers_page.expected_url, "URL Not As Expected"
        assert careers_page.is_locations_blocks_displayed(), "Locations Block Must be Displayed"
        assert careers_page.is_teams_blocks_displayed(), "Teams Block Must be Displayed"
        assert careers_page.is_life_blocks_displayed(), "Life Block Must be Displayed"
        qa_page.open_qa_page()
        assert qa_page.is_url_correct(qa_page.expected_url), "Quality Assurance PageURL Not As Expected"
        qa_page.click_see_all_qa_job_button()
        assert op_page.is_url_correct(op_page.expected_url), "Open Position PageURL Not As Expected"
        op_page.wait_until_qa_department_op()
        op_page.click_filter_combo("location")
        assert op_page.getting_location_actual_combo_set() == op_page.EXPECTED_LOCATIONS_SET, "Location Combo List Not As Expected"
        op_page.selecting_combo_list_option("Istanbul, Turkey")
        # time.sleep(3)
        op_page.wait_until_reload()
        assert op_page.are_listed_jobs_correct(), "Open Positions are not Correctly Listed"
        op_page.hover_and_click_view_role()
        op_page.switch_to_view_role()
        assert op_page.is_url_correct(op_page.view_role_url), "Job Lever PageURL Not As Expected"
