from core.activities import *
from core.locators import OnBoardingPage, LoginPage, CreateAccountPage, CommonElements

json_file_path = r"C:\Users\USER\PythonProject\FluentAI\Test Data\SignUP_Test_data\create_account_test_data.json"

with open(json_file_path, "r", encoding="utf-8") as f:
    test_data = json.load(f)



def go_to_signin_information_page(driver):

    #
    click_on(driver,OnBoardingPage.try_now_button)

    #Need to click on the continue button
    for i in range(2) :
        click_on(driver,OnBoardingPage.continue_button)


def go_to_CreateYourAccountPage(driver):

    click_on(driver,LoginPage.signup_button)


def go_to_otp_verification_page(driver):

    go_to_CreateYourAccountPage(driver)
    for data in test_data['valid_number'] :

        number=data['phone']
        fill_input_field(driver,CommonElements.input_filed,number)
        click_on(driver,CommonElements.continue_button)

