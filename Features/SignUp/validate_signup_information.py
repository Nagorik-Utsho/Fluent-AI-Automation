from logging import exception

from appium.webdriver.extensions.android.common import Common
from pandas.core.reshape.util import tile_compat

from core.activities import fill_input_field, scroll_and_collect_all_elements, click_on, match_element, \
    collect_on_screen_items
from core.locators import CommonElements, Android, InformationPage
from core.report_generator import save_to_csv

def validate_title(driver,actual_xpath,target_title):
    check_title=match_element(driver,actual_xpath,target_title)

    return check_title

def validate_input_field(driver,name):

    fill_input_field(driver,CommonElements.input_filed,name)
    click_on(driver,Android.android_NextButton)



def validate_onscreen_items(driver,english_level):


    #Target english level selection
    #title_match=match_element(driver,InformationPage.title_level_english,"What is your level of English")

    #match_element
    level_match=match_element(driver, InformationPage.interest_found(english_level), f"{english_level}")

    return level_match



def validate_all_collection(driver, expected_data,key_name):


    # Collect all UI interests
    result = scroll_and_collect_all_elements(driver)
    print(result['elements'])
    ui_interests = set(result['elements'])


    # Prepare expected interests
    expected_interests = set([item[key_name] for item in expected_data])

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


def validate_select_deselect_functionality(driver,interest,selected):

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


