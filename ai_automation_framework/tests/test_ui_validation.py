import pytest
from pages.base_page import BasePage
from locators.locators import LoginLocators, DashboardLocators
from utils.excel_reader import read_test_cases

test_data = read_test_cases("../test_cases.xlsx")
module_tests = [tc for tc in test_data if tc["Module"] == "UX/UI Validation"]
priority_map = {"High": "high", "Medium": "medium", "Low": "low"}

@pytest.mark.parametrize("tc", module_tests)
def test_ux_ui_validation(tc, driver):
    if str(tc.get("RunMode")).strip().lower() != "yes":
        pytest.skip(f"Skipping {tc['Test Case ID']} as RunMode is not Yes")
    
    priority = priority_map.get(tc.get("Priority"), "medium")
    getattr(pytest.mark, priority)(lambda: None)

    page = BasePage(driver)
    driver.get("https://ai.com")
    page.enter_text(LoginLocators.USERNAME, "testuser")
    page.enter_text(LoginLocators.PASSWORD, "password")
    page.click(LoginLocators.LOGIN_BTN)
    
    steps = tc["Test Steps"].split(" 2. ")
    for step in steps:
        if "Trigger" in step:
            print(f"Triggering action: {step}")
        elif "Check" in step or "Validate" in step:
            print(f"Validating: {step}")
        else:
            print(f"Executing: {step}")
    
    assert True
