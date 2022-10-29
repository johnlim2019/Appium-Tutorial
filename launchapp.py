# time
import time

# appium drivers and services
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


# desired capabilities
caps = {}
caps["appium:appPackage"] = "com.code2lead.kwad"
caps["appium:appActivity"] = "com.code2lead.kwad.MainActivity"
caps["platformName"] = "Android"
caps["appium:deviceName"] = "Lim Jie Sheng's S21 FE"
caps["appium:udid"] = "RFCT41V8Y9V"
caps["appium:uiautomator2ServerInstallTimeout"] = 5000
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", caps)
print(driver.session_id+"\n____________________________________\n")


enter_some_val_button = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Btn1"]')
contact_us_button = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Btn2"]')
scroll_button = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Btn3"]')
tab_activity_button = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Btn4"]')
zoom_activity = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Btn5"]')
login_activity = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Btn6"]')
long_click = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Btn7"]')
time_activity = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Btn8"]')
date_activity = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Btn9"]')

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(0,2000)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(0,1000)
actions.w3c_actions.pointer_action.release()
actions.perform()

hybrid_activity = driver.find_element(AppiumBy.XPATH,'(//android.widget.Button[@content-desc="Btn10"])[1]')
pinch_in_out = driver.find_element(AppiumBy.XPATH,'(//android.widget.Button[@content-desc="Btn10"])[2]')
drag_drop = driver.find_element(AppiumBy.XPATH,'(//android.widget.Button[@content-desc="Btn10"])[3]')
crash = driver.find_element(AppiumBy.XPATH,'(//android.widget.Button[@content-desc="Btn10"])[4]')
auto_suggestion = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[13]')

auto_suggestion.click()
time.sleep(1)

# Auto Complete 
text_input = driver.find_element(AppiumBy.ID,'com.code2lead.kwad:id/multiAutoCompleteTextView')
submit_btn = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "com.code2lead.kwad:id/btn_submit")
text_view = driver.find_elements(AppiumBy.XPATH,'//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.TextView')
expected = 'Help Lah!'
text_input.click().send_keys(expected)
submit_btn.click()
assert text_view.text == expected 

time.sleep(5)
# close the driver and service 
driver.quit()

