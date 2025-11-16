# def validate_PageTitle(driver):
from core.activities import *
from core.locators import CommonElements, CreateAccountPage


def validate_phone_number(driver , number , expected_message):

    fill_input_field(driver,CommonElements.input_filed,number)
    click_on(driver,CommonElements.continue_button)
    check_message=match_element(driver,CreateAccountPage.message,expected_message)
    return check_message






