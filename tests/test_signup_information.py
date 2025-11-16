from selenium.webdriver.common.by import By

from core.page_navigation import *
from Features.SignUp.validate_signup_information import *
import pytest_check as check  # ✅ Soft assertion library

import json

from core.locators import OnBoardingPage

json_file_path = r"/Test Data/SignUP_Test_data\information_test_data.json"


with open(json_file_path, "r", encoding="utf-8") as f:
    test_data = json.load(f)



# def test_signin_information(driver):
#
#     print("mother run")
#     go_to_signin_information_page(driver)




def test_validate_name(driver):
    """
    Validates name input field for all invalid name test cases (soft assertions).
    """
    go_to_signin_information_page(driver)

    for data in test_data["invalid_name_data"]:
        tcd = data['test_case_id']
        name = data['name']
        expected = data['expected']

        print(f"\n🔍 [TC-{tcd}] Testing name: '{name}' (Expected: {expected})")

        result = validate_input_field(driver, name)



        # ✅ Soft assertion — test continues even if it fails
        check.equal(result, expected,
                    f"❌ [FAILED] Test Case {tcd}: Name '{name}' validation mismatch — "
                    f"Expected: {expected}, Got: {result}")

        print(f"✅ [COMPLETED] Test Case {tcd}: Name '{name}' checked (Expected: {expected}, Got: {result})")
        if result == "True":
            click_on(driver,Android.android_BackNavigation)
            click_on(driver,OnBoardingPage.continue_button)




def go_to_interest_input_field(driver):

    #go to sign in page
    go_to_signin_information_page(driver)


    for data in test_data["valid_name_tests"] :
        name = data['name']
        fill_input_field(driver,CommonElements.input_filed,name)
        click_on(driver,Android.android_NextButton)


def test_validate_interest_field(driver):

    #Go to signin page
    go_to_signin_information_page(driver)
    #Go to interest input field
    go_to_interest_input_field(driver)



    failed_tests = []
    #Interest Data
    result=validate_all_collection(driver, test_data['interest_set'],'interest')
    # Log matched items
    print(f"Matched interests ({len(result['matched'])}): {result['matched']}")

    # Assertions for automated testing
    assert len(result["missing"]) == 0, f"Missing interests in UI: {result['missing']}"
    assert len(result["extra"]) == 0, f"Unexpected interests in UI: {result['extra']}"

    #Click on the search bar and Input value
    #click_on(driver, InformationPage.interest_more_button)


    # Checking the searching for valid values

    for value in test_data['interest_set']:
     search_value = value["interest"]
     expected = value["expected"]  # True for valid values
     print(f"Going to search for {search_value}")
     result = validate_interest_search_functionality(driver, search_value)
     assert result == expected, f"Search for '{search_value}' failed validation."
     print(f"[PASSED] Valid search '{search_value}' worked as expected.")

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

    #click_on(driver, InformationPage.interest_more_button)

    # ✅ First group: max 4 selectable interests
    selectable_interests = test_data['interest_set'][:4]
    #  Validating interest selection
    for i, value in enumerate(selectable_interests ):
        interest = value["interest"]
        expected = value["expected"]
        print(f"🔍 Going to search for '{interest}'")

        try:
            # Pass i+1 because the count starts from 1
            result = validate_select_deselect_functionality(driver, interest, i + 1)

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


    # shuffled_interests = random.sample(selectable_interests, k=len(selectable_interests))
    # print(shuffled_interests)

    #Deselct the selected  interests
    num_items=len(selectable_interests)
    print(selectable_interests)

    print("Going to decrease the number of deselecting")

    #  Validating deselecting interest selection
    for i, value in enumerate(selectable_interests ):
            interest = value["interest"]
            expected = value["expected"]
            print(f"🔍 Going to search for '{interest}'")
            decrease=(num_items-(i+1))
            print(f"Decrement number is : {decrease}")
            try:
                # Pass i+1 because the count starts from 1
                result = validate_select_deselect_functionality(driver, interest, decrease)

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

    #select Interest and move forward


# Load JSON test data

def go_to_english_level(driver):
    go_to_interest_input_field(driver)
    for data in test_data["valid_interest"]:
        interest=data['interest']
        click_on(driver,InformationPage.interest_found(interest) )
        click_on(driver,Android.android_NextButton)




def test_english_level(driver):
    """
    Test that all English levels from the test data are correctly displayed on the screen.
    """
    #Go to english level
    go_to_english_level(driver)

    for data in test_data['english_level_set']:
        english_level = data['level']
        expected = data['expected']

        # Call the validation function
        result = validate_onscreen_items(driver, english_level)

        # Assertion to ensure the test fails if validation doesn't match expected
        assert result == expected, f"❌ Validation failed for English level '{english_level}': expected {expected}, got {result}"

        # Optional: log success
        print(f"✅ [PASSED] English level '{english_level}' validation matched expected: {expected}")




def go_to_area_of_improve(driver):
    go_to_english_level(driver)
    #English level selection
    click_on(driver,InformationPage.beginner_level)
    click_on(driver,Android.android_NextButton)





def test_area_of_improve(driver):

    go_to_area_of_improve(driver)

    click_on(driver,InformationPage.area_more_button)
    #Match the title
    # result=validate_title(driver,InformationPage.area_title,"Area")
    # assert result == True, f"❌ Validation failed for Improve Area Title Match"


    result=validate_all_collection(driver, test_data['area_data'],'area')
    # Log matched items
    print(f"Matched  ({len(result['matched'])}): {result['matched']}")

    # Assertions for automated testing
    assert len(result["missing"]) == 0, f"Missing interests in UI: {result['missing']}"
    assert len(result["extra"]) == 0, f"Unexpected interests in UI: {result['extra']}"


def go_to_goal_time(driver) :
    go_to_area_of_improve(driver),
    for data in test_data['valid_area']:
        area=data['area']
        click_on(driver,InformationPage.interest_found(area))
        click_on(driver,Android.android_NextButton)



def test_goal_time(driver):

    go_to_goal_time(driver)
    #Match the title
   # result = validate_title(driver, InformationPage.area_title, "Area")
    #assert result == "True", f"❌ Validation failed for Improve Area Title Match"
    click_on(driver, InformationPage.interest_more_button)
    result = validate_all_collection(driver, test_data['time_goal_data'],'time')
    # Log matched items
    print(f"Matched Goal Time ({len(result['matched'])}): {result['matched']}")

    # Assertions for automated testing
    assert len(result["missing"]) == 0, f"Missing interests in UI: {result['missing']}"
    assert len(result["extra"]) == 0, f"Unexpected interests in UI: {result['extra']}"



def go_to_time_selection(driver):
    go_to_goal_time(driver)

    for data in test_data['valid_time']:
        time=data['time']
        click_on(driver,InformationPage.interest_found(time))
        click_on(driver,Android.android_NextButton)









def test_click__time(driver) :
    go_to_time_selection(driver)
    click_on(driver,Android.android_NextButton)
    click_on(driver,InformationPage.final_continue_button)














