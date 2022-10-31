import pytest
import unittest
import allure
from KWA_demo_commands import DemoCommands
from qaseio.pytest import qase


@pytest.mark.usefixtures('createClassDriver')
class test_KWA_Demo(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setupClassObject(self):
        self.commands = DemoCommands(self.driver, __file__)
        yield 
        # if we are not at the homepage, go back, check by looking for the title after scrolling to the top
        self.commands.scrollUp(600)
        if self.commands.isDisplayed('Appium Demo') != True:
            self.commands.systemBackBtn()
    @qase.title('testHomepage')
    def test_Homepage(self):
        self.commands.testHomepage()

    @qase.title('testEnterSomeValue')        
    def test_EnterSomeValue(self):
        self.commands.testEnterSomeValue()
    
    @qase.title('testContactForm')
    def test_contactForm(self):
        self.commands.testContactForm()
    
    @qase.title('testFailGetElement')
    def test_failGetElement(self):
        self.commands.testFailGetElement()
    
    @qase.title('testFailGetElementFromElements')       
    def test_failGetElementFromElements(self):
        self.commands.testFailGetElementFromElements()

