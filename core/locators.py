from core.necessary_packages import *


class Android:
    android_BackNavigation=(By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button[1]')
    android_NextButton=(By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView')

class CommonElements :
    input_filed=(By.CLASS_NAME,'android.widget.EditText')

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









