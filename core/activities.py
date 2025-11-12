import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from core.locators import InformationPage
from core.necessary_packages import *
def fill_input_field(driver, locator, value, index=0, timeout=30):
    """
    Clicks, clears, and sends keys to an input field at a given index.
    """
    wait = WebDriverWait(driver, timeout)
    fields = wait.until(EC.presence_of_all_elements_located(locator))
    if len(fields) <= index:
        raise Exception(f"Not enough input fields found (index {index})")
    field = fields[index]
    field.click()
    time.sleep(0.5)
    field.clear()
    field.send_keys(value)
    return field


import time
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def click_on(driver, locator_value, timeout=30, max_retries=3):
    """
    Clicks on an element safely, retrying if it becomes stale.

    Parameters:
        driver: Appium/Selenium driver
        locator_value: tuple like (By.XPATH, 'xpath_here')
        timeout: seconds to wait for element presence
        max_retries: number of retry attempts if element is stale
    """
    attempt = 0
    while attempt < max_retries:
        try:
            wait = WebDriverWait(driver, timeout)
            field = wait.until(EC.presence_of_element_located(locator_value))
            time.sleep(0.5)  # optional small pause before click
            field.click()
            return True
        except StaleElementReferenceException:
            attempt += 1
            print(f"[Warning] StaleElementReferenceException encountered. Retry {attempt}/{max_retries}")
            time.sleep(1)  # wait before retrying
        except TimeoutException:
            print(f"[Error] Element not found within {timeout} seconds: {locator_value}")
            raise
    # If still fails after retries
    raise StaleElementReferenceException(f"Failed to click on element after {max_retries} retries: {locator_value}")


def match_element(driver, locator_value, expected_text, timeout=5):
    wait = WebDriverWait(driver, timeout)
    field = wait.until(EC.presence_of_element_located(locator_value))

    actual_text = field.get_attribute('content-desc') or field.text
    actual_text = actual_text.strip().lower()
    print(actual_text)
    expected_text = expected_text.strip().lower()  # Assign the cleaned value

    if  expected_text in actual_text:
        return True
    else:
        print(f"Actual Text   : {actual_text}")
        print(f"Expected Text : {expected_text}")
        return False



def scroll_and_collect_all_elements(driver,max_scrolls_per_direction=10, max_cycles=5):
    """
    Scrolls through a ScrollView and collects all element names
    whose XPath matches //android.view.View[contains(@content-desc, "")].
    Returns a dict with status and collected element names.
    """
    print("🔍 Collecting android.view.View elements (with content-desc) from ScrollView...")
    InformationPage.interest_scroller = "//android.widget.ScrollView"

    possible_scrollviews = [
        InformationPage.interest_scroller

    ]

    wait = WebDriverWait(driver, 60)
    scrollable = None
    scrollview_xpath = None

    # Try to locate any valid scrollview
    for xpath in possible_scrollviews:
        try:
            scrollable = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, xpath)))
            scrollview_xpath = xpath
            break
        except TimeoutException:
            print(f"⚠️ ScrollView not found with xpath: {xpath}")

    if not scrollable:
        print("❌ No valid ScrollView container found.")
        return {"status": "FAILED", "message": "No valid ScrollView container found"}

    collected_elements = set()
    directions = ["down"]

    for cycle in range(max_cycles):

        for direction in directions:
            for attempt in range(max_scrolls_per_direction):
                try:
                    scrollable = driver.find_element(AppiumBy.XPATH, scrollview_xpath)

                    # 🔹 Collect elements with the desired XPath shape
                    visible_elements = scrollable.find_elements(
                        AppiumBy.XPATH,".//android.view.View[contains(@content-desc,'')]")

                    for el in visible_elements:
                        try:
                            name = el.get_attribute("content-desc")
                            if name and name.strip():
                                collected_elements.add(name.strip())
                        except Exception:
                            pass

                    # 🔹 Scroll further
                    driver.execute_script("mobile: scrollGesture", {
                        "elementId": scrollable.id,
                        "direction": direction,
                        "percent": 0.5,
                        "duration":2000
                    })
                    #time.sleep(0.5)

                except StaleElementReferenceException:
                    print("⚠️ ScrollView went stale, retrying...")

    print(f"✅ Collected {len(collected_elements)} unique android.view.View elements.")
    return {
        "status": "SUCCESS",
        "elements": list(collected_elements)
    }


def scroll_in_scrollview(driver, max_scrolls_per_direction=1, max_cycles=1):
    """
    Scroll up and down in a ScrollView.
    Returns a dict with status and message.
    """
    print("🔄 Starting to scroll in ScrollView...")

    scrollview_xpath = '//android.widget.ScrollView'

    try:
        wait = WebDriverWait(driver, 60)
        scrollable = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, scrollview_xpath)))
    except TimeoutException:
        print("❌ ScrollView not found.")
        return {"status": "FAILED", "message": "ScrollView container not found"}

    directions = ["down"]

    for cycle in range(max_cycles):
        for direction in directions:
            for attempt in range(max_scrolls_per_direction):
                try:
                    scrollable = driver.find_element(AppiumBy.XPATH, scrollview_xpath)
                    driver.execute_script("mobile: scrollGesture", {
                        "elementId": scrollable.id,
                        "direction": direction,
                        "percent": 0.8
                    })
                    print(f"➡️ Scrolled {direction} (cycle {cycle + 1}, attempt {attempt + 1})")
                    time.sleep(0.5)
                except StaleElementReferenceException:
                    print("⚠️ ScrollView went stale, retrying...")

    print("✅ Finished scrolling.")
    return {"status": "SUCCESS", "message": "Scroll completed"}


def swipe_up_mobile(driver):
    print("Mobile swipe ")
    driver.execute_script("mobile: scrollGesture", {
        "direction": "up",
        # optionally: scroll inside a container element
        # "elementId": container_element.id,
        "percent": 0.8
    })
    time.sleep(0.5)


def screen_swipe_gesture (driver):
    print("Screen gestrue")
    size = driver.get_window_size()
    start_x = size['width'] / 2
    start_y = size['height'] * 0.8
    end_y = size['height'] * 0.2

    driver.execute_script("mobile: swipeGesture", {
        "startX": start_x,
        "startY": start_y,
        "endX": start_x,
        "endY": end_y,
        "speed": 800
    })
    time.sleep(0.5)






