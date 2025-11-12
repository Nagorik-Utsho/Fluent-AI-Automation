from core.activities import *
from core.locators import OnBoardingPage


def go_to_signin_information_page(driver):

    #
    click_on(driver,OnBoardingPage.try_now_button)

    #Need to click on the continue button
    for i in range(2) :
        click_on(driver,OnBoardingPage.continue_button)
