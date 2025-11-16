import os

from Features.SignUp.validate_AccountCreation import *
from core.page_navigation import go_to_CreateYourAccountPage, go_to_otp_verification_page
import pytest_check as check
import json


json_file_path = r"C:\Users\USER\PythonProject\FluentAI\Test Data\SignUP_Test_data\create_account_test_data.json"

with open(json_file_path, "r", encoding="utf-8") as f:
    test_data = json.load(f)



def test_phone_number(driver):

    go_to_CreateYourAccountPage(driver)

    for data in test_data['number_test_data']:

        number=data['phone']
        tcd=data['test_case_id']
        message=data['message']
        expected=data['expected']

        result=validate_phone_number(driver, number,message)

        # Soft assertion
        check.equal(result, expected,
                    f"❌ Test Case {tcd} failed for input '{number}': expected {expected}, got {result}")

        # Log success with green check mark if passed
        if result == expected:
            print(f"\033[92m✅ Test Case {tcd} passed for input '{number}': got expected {result}\033[0m")







def test_otp_verification_page(driver):
    go_to_otp_verification_page(driver)

    for data in test_data['invalid_otp_test_data'] :
        otp=data['otp']
        tcd=['test_case_id']







