from logging import exception

from appium.webdriver.extensions.android.common import Common

from core.activities import fill_input_field, scroll_and_collect_all_elements, click_on, match_element
from core.locators import CommonElements, Android, InformationPage
from core.report_generator import save_to_csv


def validate_name_input_field(driver,name):


    fill_input_field(driver,CommonElements.input_filed,name)
    click_on(driver,Android.android_NextButton)


def validate_all_interests(driver, expected_interests_data):
    click_on(driver, InformationPage.interest_more_button)

    # Collect all UI interests
    result = scroll_and_collect_all_elements(driver)
    ui_interests = set(result['elements'])


    # Prepare expected interests
    expected_interests = set([item['interest'] for item in expected_interests_data])

    # Compare sets
    missing_in_ui = expected_interests - ui_interests  # Expected but not in UI
    extra_in_ui = ui_interests - expected_interests  # In UI but not expected
    matched = expected_interests & ui_interests  # Correctly matched items


    # Return all sets for assertions
    return {
        "matched": matched,
        "missing": missing_in_ui,
        "extra": extra_in_ui
    }

def validate_interest_search_functionality(driver , search_value ):




    fill_input_field(driver,InformationPage.search_bar,search_value)

    check_interest = match_element(driver,InformationPage.interest_found(search_value),search_value)

    interest_found= check_interest

    return interest_found


def validate_interest_select_deselect_functionality(driver,interest,selected):

    fill_input_field(driver,InformationPage.search_bar,interest)

    #Click on the Interest
    click_on(driver,InformationPage.interest_found(interest))
    check_selected_number = match_element(driver,InformationPage.selected_interest(selected),f"{selected}/4 selected")




    return check_selected_number


def validate_no_interest_selected(driver):

    #click on the next without selecting interest
    click_on(driver,Android.android_NextButton)

    #Match the pop-up
    check_message=match_element(driver,InformationPage.no_answer_popup,"Info Please select your answer")

    return check_message


