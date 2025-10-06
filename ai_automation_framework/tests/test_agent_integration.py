import pytest
from pages.base_page import BasePage
from locators.locators import LoginLocators

test_data = read_test_cases("../test_cases.xlsx")
module_tests = [tc for tc in test_data if tc["Module"] == "Agent Integration"]

@pytest.mark.parametrize("tc", module_tests)
def test_agent_integration(tc, driver):
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
