from core.necessary_packages import *


class Android:
    android_BackNavigation=(By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button[1]')
    android_NextButton=(By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView')

class CommonElements :
    input_filed=(By.CLASS_NAME,'android.widget.EditText')
    continue_button = (By.XPATH, '//android.widget.Button[@content-desc="Continue"]')

class OnBoardingPage:
    login_button=(By.XPATH,'//android.widget.Button[@content-desc="Log in"]')
    try_now_button=(By.XPATH,'//android.widget.Button[@content-desc="Try Now"]')
    continue_button=(By.XPATH,'//android.widget.Button[@content-desc="Continue"]')


class InformationPage:

    no_answer_popup=(By.XPATH,'//android.view.View[@content-desc="Info\nPlease select your answer"]')

    bot_chat_validation = (By.XPATH,
                "//android.widget.ImageView[@content-desc=\"I'm Flin, your personalized AI Tutor. I will help you improve your English.\"]")

    validation_message_empty_name = (By.XPATH,'//android.view.View[@content-desc="Sorry\nPlease enter your name"]')
    validation_message_over_length=(By.XPATH,'//android.view.View[@content-desc="Name cannot be more than 15 character"]')

    '''Interest Section related xpath'''
    interest_more_button=(By.XPATH,'//android.view.View[@content-desc="More..."]')
    interest_widget_title=(By.XPATH,'//android.view.View[@content-desc="Interest"]')
    interest_select_button=(By.XPATH,'//android.widget.Button[@content-desc="Select"]')
    search_bar=(By.CLASS_NAME,'android.widget.EditText')


    def selected_interest(number_of_click: int):
        xpath = f'//android.view.View[@content-desc="{number_of_click}/4 Selected"]'
        return (By.XPATH, xpath)

    interest_scroller=(By.XPATH,'//android.widget.ScrollView')
    interest_not_found=(By.XPATH,'//android.view.View[@content-desc="No interests found"]')

    def interest_found(interested_item):

           return (By.XPATH,f'//android.view.View[contains(@content-desc,"{interested_item}")]')

    #collecting from level of English

    title_level_english=(By.XPATH,'//android.widget.ImageView[@content-desc="What is your level of English"]')

    beginner_level=(By.XPATH,'//android.view.View[@content-desc="Beginner"]')
    preintermediate_level=(By.XPATH,'//android.view.View[@content-desc="Pre-Intermediate"]')
    intermediate_level=(By.XPATH,'//android.view.View[@content-desc="Intermediate"]')
    advanced_level=(By.XPATH,'//android.view.View[@content-desc="Advanced"]')

    #Areas of improvement
    area_title=(By.XPATH,'//android.view.View[@content-desc="Area"]')
    area_more_button=(By.XPATH,'//android.view.View[@content-desc="More..."]')


    #Select the time
    def hour_seek_bar(hour):

          return (By.XPATH,f'//android.widget.SeekBar[@content-desc="{hour}"]')


    def min_seek_bar(min) :

        return (By.XPATH, f'//android.widget.SeekBar[@content-desc="{min}"]')


    def meridiem_seek_bar(meridiem) :


        return (By.XPATH,f'//android.widget.SeekBar[@content-desc="{meridiem}"]')






class LoginPage:

    continue_with_google=(By.XPATH,'//android.widget.ImageView[@content-desc="Continue with Google"]')
    continue_with_password=(By.XPATH,'//android.widget.Button[@content-desc="Sign in with password"]')
    signup_button=(By.XPATH,'//android.widget.Button[@content-desc="Sign Up"]')

class CreateAccountPage :
    create_account_page_title=(By.XPATH,'//android.view.View[@content-desc="Create your account 📝"]')
    message=(By.XPATH,'//android.view.View[contains(@content-desc,"")]')
    invalid_phone_number = (By.XPATH,'' )
    create_account_page_subtitle=(By.XPATH,'//android.view.View[@content-desc="Please enter your phone number and we will send an OTP code in the next step to set you up."]')
    create_account_button=(By.XPATH,'//android.widget.Button[@content-desc="Create account"]')
    password_hidden_icon=(By.XPATH,'(//android.view.View[@content-desc="Password"])[2]/android.widget.Button')





class OTP :







