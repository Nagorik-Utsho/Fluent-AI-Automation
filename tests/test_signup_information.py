import json
import random

import pytest
from colorama import Fore
from playwright.sync_api import expect
from pytokens.cli import validate

from Features.SignIn.go_to_information_page import go_to_signin_information_page
from Features.SignIn.validate_signin_information import *


# Load JSON test data
json_file_path = r"C:\Users\USER\PythonProject\FluentAI\Test Data\SiginTest_data\interest_test_data.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    interest_test_data = json.load(f)
def test_signin_information(driver):
    failed_tests = []

    go_to_signin_information_page(driver)

    # for data in name_test_data["invalid_name_tests"] :
    #     tcd=data['test_case_id']
    #     name=data['name']
    #     expected=data['expected']

    validate_name_input_field(driver,"Utsho")

    #Interest Data
    # result=validate_all_interests(driver, interest_test_data['interest_set'])
    #
    # # Log matched items
    # print(f"Matched interests ({len(result['matched'])}): {result['matched']}")
    #
    # # Assertions for automated testing
    # assert len(result["missing"]) == 0, f"Missing interests in UI: {result['missing']}"
    # assert len(result["extra"]) == 0, f"Unexpected interests in UI: {result['extra']}"

    # Click on the search bar and Input value
    #click_on(driver, InformationPage.interest_more_button)

    # Checking the searching for valid values

    # for value in interest_test_data['interest_set']:
    #  search_value = value["interest"]
    #  expected = value["expected"]  # True for valid values
    #  print(f"Going to search for {search_value}")
    #  result = validate_interest_search_functionality(driver, search_value)
    #  assert result == expected, f"Search for '{search_value}' failed validation."
    #  print(f"[PASSED] Valid search '{search_value}' worked as expected.")

    # Attempt to validate moving forward without selecting interest
    try:

        result = validate_no_interest_selected(driver)

        if result:
            print("✅ User could not move forward without selecting an interest (as expected).")
        else:
            print("❌ User was able to move forward without selecting an interest!")

    except Exception as e:
        # Graceful handling of unexpected exceptions
        print("⚠️ Exception occurred while validating no interest selected:")
        print(f"   ↳ {str(e).splitlines()[-1]}")
        result = False  # Treat as failed validation

    click_on(driver, InformationPage.interest_more_button)

    # ✅ First group: max 4 selectable interests
    selectable_interests = interest_test_data['interest_set'][:4]
    #  Validating interest selection
    for i, value in enumerate(selectable_interests ):
        interest = value["interest"]
        expected = value["expected"]
        print(f"🔍 Going to search for '{interest}'")

        try:
            # Pass i+1 because the count starts from 1
            result = validate_interest_select_functionality(driver, interest, i + 1)

            if result == expected:
                print(f"✅ [PASSED] '{interest}' worked as expected ({i + 1}/4 selected).")
            else:
                print(f"❌ [FAILED] '{interest}' result mismatch. Expected {expected}, got {result}.")
                failed_tests.append(interest)

        except Exception as e:
            # Graceful handling of 5th selection or any unexpected error
            print(f"⚠️ [EXCEPTION] Could not select '{interest}' (probably max 4 interests allowed).")
            print(f"   ↳ Error: {str(e).splitlines()[-1]}")  # short message
            failed_tests.append(interest)

    # After loop ends, summarize results
    if failed_tests:
        print("\n🚨 TEST SUMMARY: Some tests failed.")
        print("Failed interests:", ", ".join(failed_tests))
    else:
        print("\n✅ ALL TESTS PASSED SUCCESSFULLY.")



    #Deselct the selected  interests
    num_items=len(selectable_interests)
    print(selectable_interests)
    #  Validating deselecting interest selection
    for i, value in enumerate(selectable_interests):
            interest = value["interest"]
            expected = value["expected"]
            print(f"🔍 Going to search for '{interest}'")
            decrease=num_items-i
            print(f"Decrement number is : {decrease}")
            try:
                # Pass i+1 because the count starts from 1
                result = validate_interest_select_functionality(driver, interest, decrease)

                if result == expected:
                    print(f"✅ [PASSED] '{interest}' worked as expected ({decrease}/4 selected).")
                else:
                    print(f"❌ [FAILED] '{interest}' result mismatch. Expected {expected}, got {result}.")
                    failed_tests.append(interest)

            except Exception as e:
                # Graceful handling of 5th selection or any unexpected error
                print(f"⚠️ [EXCEPTION] Could not select '{interest}' (probably max 4 interests allowed).")
                print(f"   ↳ Error: {str(e).splitlines()[-1]}")  # short message
                failed_tests.append(interest)

    # After loop ends, summarize results
    if failed_tests:
            print("\n🚨 TEST SUMMARY: Some tests failed.")
            print("Failed interests:", ", ".join(failed_tests))
    else:
            print("\n✅ ALL TESTS PASSED SUCCESSFULLY.")










