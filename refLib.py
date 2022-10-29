# for logger
import inspect
import logging

# for operations class
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# For wait for element
from selenium.common.exceptions import (
    ElementNotVisibleException,
    ElementNotSelectableException,
    NoSuchElementException,
)
from selenium.webdriver.support.wait import WebDriverWait


def getDriver():
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
    caps[
        "app"
    ] = r"C:\SUTD-ONEDRIVE\internshit\appium\Touchscreen Tests\Android_Demo_App.apk"

    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)


def loggerBuild(fileName):
    logName = inspect.stack()[1][3]  # one is the name record of the function calling, then third element is the name
    logger = logging.getLogger(logName)
    logger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler("{0}.log".format(fileName), mode="a")
    fileHandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s : %(message)s",
        datefmt="%d/%m/%y %I:%M:%S %p %A",
    )
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger


class OperationsFramework:
    def __init__(self, driver, file):
        # basically we always want to ue the same driver object when we call all our tests in the module.
        self.driver = driver
        self.actions = ActionChains(driver)
        self.log = loggerBuild(file)

    def scrollDown(actions, driver, distance):
        actions.w3c_actions = ActionBuilder(
            driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
        )
        actions.w3c_actions.pointer_action.move_to_location(0, 2000)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(0, 2000 - distance)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def scrollUp(self, distance):
        self.actions.w3c_actions = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
        )
        self.actions.w3c_actions.pointer_action.move_to_location(0, 2000)
        self.actions.w3c_actions.pointer_action.pointer_down()
        self.actions.w3c_actions.pointer_action.move_to_location(0, 2000 - distance)
        self.actions.w3c_actions.pointer_action.release()
        self.actions.perform()

    def systemBackBtn(self):
        self.driver.press_keycode(4)

    def waitForElement(self, locatorValue, locatorType, timeout=25):
        locatorType = locatorType.lower().strip()
        element = None
        wait = WebDriverWait(self.driver, timeout, poll_frequency=1, ignored_exceptions=[
                             ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException])
        if locatorType == 'id':
            element = wait.until(lambda x: x.find_element(AppiumBy.ID, locatorValue))
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locatorValue))
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().description("%s")' % (locatorValue)))
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(%d)" % int(locatorValue)))
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'UiSelector().textContains("%s")' % locatorValue))
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '%s' % (locatorValue)))
        else:
            self.log.info(locatorType + " type not in state machine")
        return element

    def getElement(self, locatorValue, locatorType='text'):
        element = None
        try:
            locatorType = locatorType.lower().strip()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info("Element with locator value '" + locatorValue +
                          "' of locator type '" + locatorType + "' is found")
            return element
        except:
            self.log.info("Locator value '" + locatorValue + "' of '" + locatorType + "' type not found")
        return element
    
    def waitForElements(self,locatorValue, locatorType, timeout=25):
        locatorType = locatorType.lower().strip()
        elements = None
        wait = WebDriverWait(self.driver, timeout, poll_frequency=1, ignored_exceptions=[
                             ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException])
        if locatorType == 'id':
            elements = wait.until(lambda x: x.find_elements(AppiumBy.ID, locatorValue))
        elif locatorType == "class":
            elements = wait.until(lambda x: x.find_elements(AppiumBy.CLASS_NAME, locatorValue))
        elif locatorType == "des":
            elements = wait.until(
                lambda x: x.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().description("%s")' % (locatorValue)))
        elif locatorType == "index":
            elements = wait.until(
                lambda x: x.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(%d)" % int(locatorValue)))
        elif locatorType == "text":
            elements = wait.until(lambda x: x.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'UiSelector().textContains("%s")' % locatorValue))
        elif locatorType == "xpath":
            elements = wait.until(lambda x: x.find_elements(AppiumBy.XPATH, '%s' % (locatorValue)))
        else:
            self.log.info(locatorType + " type not in state machine")
        return elements
    
    def getElementFromElements(self,locatorValue,locatorType='text',index=0):
        element = None
        try:
            locatorType = locatorType.lower().strip()
            elements = self.waitForElements(locatorValue, locatorType)
            print('elements in getElementFromElements()')
            print(elements)
            element = elements[index]
            print(elements[0])
            # self.log.info(elements.length + " elements with 'locator value '" + locatorValue +"' of locator type '" + locatorType + "' is found")
            return element
        except:
            self.log.info("0 elements of locator value '" + locatorValue + "' of '" + locatorType + "' type not found")
        return element

    def clickElement(self, locatorValue, locatorType="text"):
        element = None
        try:
            locatorType = locatorType.lower().strip()
            element = self.getElement(locatorValue, locatorType)
            element.click()
            self.log.info(
                "Clicked on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to click on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)

    def sendText(self, text, locatorValue, locatorType="text"):
        element = None
        try:
            locatorType = locatorType.lower().strip()
            element = self.getElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(
                "Send text  on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)


    def isDisplayed(self, locatorValue, locatorType="text"):
        element = None
        if (type(locatorValue) != str): 
            try:
                locatorValue.is_displayed()
                self.log.info(
                    "Given XML object is displayed")
                return True
            except:
                self.log.info(
                    "Given XML object is not displayed")
                return False

        else: 
            try:
                locatorType = locatorType.lower().strip()
                element = self.getElement(locatorValue, locatorType)
                element.is_displayed()
                self.log.info(
                    "Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + "is displayed ")
                return True
            except:
                self.log.info(
                    "Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + " is not displayed")
                return False
    
    def screenShot(self, screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path : " + screenshotPath)

        except:
            self.log.info("Unable to save Screenshot to the Path : " + screenshotPath)
