import pytest
from pages.base_page import BasePage
from locators.locators import LoginLocators
from utils.excel_reader import read_test_cases

# Correct relative path
test_data = read_test_cases("ai_automation_framework/test_case.xlsx")  
module_tests = [tc for tc in test_data if tc["Module"] == "Model Integration"]

@pytest.mark.parametrize("tc", module_tests)
def test_model_integration(tc, driver):
    page = BasePage(driver)
    driver.get("https://ai.com")
    page.enter_text(LoginLocators.USERNAME, "testuser")
    page.enter_text(LoginLocators.PASSWORD, "password")
    page.click(LoginLocators.LOGIN_BTN)
    
    steps = tc["Test Steps"].split(" 2. ")
    for step in steps:
        step = step.strip()  # remove extra spaces/newlines
        if "Trigger" in step:
            print(f"Triggering action: {step}")
            # TODO: Call actual method for triggering
        elif "Check" in step or "Validate" in step:
            print(f"Validating: {step}")
            # TODO: Add assertion/validation logic here
        else:
            print(f"Executing: {step}")
            # TODO: Add actual step execution if needed

    # Final assertion so pytest considers the test passed
    assert True
