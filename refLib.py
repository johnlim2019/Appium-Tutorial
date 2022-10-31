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

# for allure report
import allure

# for qase integration
from qaseio.pytest import qase

def allureSteps(text):
    with allure.step(text):
        time.sleep(1)
        pass

def reportSteps(text):
    with qase.step(text):
        time.sleep(1)
        pass

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
    # one is the name record of the function calling, then third element is the name
    logName = inspect.stack()[1].function
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

    def scrollDown(self, distance):
        self.actions.w3c_actions = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
        )
        self.actions.w3c_actions.pointer_action.move_to_location(0, 600)
        self.actions.w3c_actions.pointer_action.pointer_down()
        self.actions.w3c_actions.pointer_action.move_to_location(0, 600 - distance)
        self.actions.w3c_actions.pointer_action.release()
        self.actions.perform()

    def scrollUp(self, distance):
        self.actions.w3c_actions = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
        )
        self.actions.w3c_actions.pointer_action.move_to_location(0, 600)
        self.actions.w3c_actions.pointer_action.pointer_down()
        self.actions.w3c_actions.pointer_action.move_to_location(0, 600 + distance)
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
            err = "Locator value '" + locatorValue + "' of '" + locatorType + "' type not found"
            self.log.info(err)
            self.reportErrScreenshot('getElement')
            return element

    def waitForElements(self, locatorValue, locatorType, timeout=25):
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

    def getElementFromElements(self, locatorValue, locatorType='text', index=0):
        element = None
        try:
            locatorType = locatorType.lower().strip()
            elements = self.waitForElements(locatorValue, locatorType)
            # print('elements in getElementFromElements()')
            # print(elements)
            element = elements[index]
            # print(elements[0])
            self.log.info('index: '+index + " element with 'locator value '" +
                          locatorValue + "' of locator type '" + locatorType + "' is found")
            return element
        except:
            err = "No elements of locator value '" + locatorValue + "' of '" + locatorType + "' type not found"
            self.log.info(err)
            self.reportErrScreenshot('getElementFromElements')
            return element

    def clickElement(self, locatorValue, locatorType="text"):
        element = None
        try:
            locatorType = locatorType.lower().strip()
            element = self.getElement(locatorValue, locatorType)
            element.click()
            self.log.info(
                "Clicked on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            return element
        except:
            err = "Unable to click on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue
            self.log.info(err)
            self.reportErrScreenshot('clickElement')
            return element

    def sendText(self, text, locatorValue, locatorType="text"):
        element = None
        try:
            locatorType = locatorType.lower().strip()
            element = self.getElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(
                "Send text  on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            err = "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue
            self.log.info(err)
            self.reportErrScreenshot('sendText')
            assert False

    def isDisplayed(self, locatorValue, locatorType="text", el=None):
        element = None
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

    def isDisplayedElement(self, Element):
        try:
            Element.is_displayed()
            self.log.info(
                "Given XML object is displayed")
            return True
        except:
            self.log.info(
                "Given XML object is not displayed")
            return False

    def hasAttribute(self, expectedValue, attribute, locatorValue=None, locatorType='text', element=None, includes=True):
        expectedValue = expectedValue.strip()
        actualValue = None
        if element != None:
            actualValue = element.get_attribute(attribute).strip()
        else:
            actualValue = self.getElement(locatorValue, locatorType).get_attribute(attribute).strip()
        if includes == True:
            result = (expectedValue in actualValue)
        else:
            result = (expectedValue == actualValue)
        if result:
            if (element == None):
                self.log.info('For locator value: "'+locatorValue+'" of locator type: "' +
                              locatorType+'"\nActual:'+actualValue+' matches Expected:'+expectedValue)
            else:
                self.log.info('In given element, Actual:'+actualValue+' matches Expected:'+expectedValue)
        else:
            if (element == None):
                self.log.info('For locator value: "'+locatorValue+'" of locator type: "'+locatorType +
                              '"\nActual:'+actualValue+' does not match Expected:'+expectedValue)
            else:
                self.log.info('In given element, Actual:'+actualValue+' does not matches Expected:'+expectedValue)
        return result

    def screenShot(self, screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "./screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path : " + screenshotPath)
            return screenshotPath
        except:
            self.log.info("Unable to save Screenshot to the Path : " + screenshotPath)

    def reportErrScreenshot(self, name):
        imageFile = self.screenShot(name)
        allure.attach.file(imageFile, attachment_type=allure.attachment_type.PNG)
        qase.attach(imageFile)
   