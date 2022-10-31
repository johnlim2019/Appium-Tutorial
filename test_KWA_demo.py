import pytest
import unittest
import allure
from KWA_demo_commands import DemoCommands


@pytest.mark.usefixtures('createClassDriver')
class test_KWA_Demo(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setupClassObject(self):
        self.commands = DemoCommands(self.driver,__file__)
        allure.allureLogs('set up driver for each test')
    @pytest.mark.order(1)
    def test_Homepage(self):
        self.commands.testHomepage()
    @pytest.mark.order(2)    
    @pytest.mark.skip
    def test_EnterSomeValue(self):
        self.commands.testEnterSomeValue()
    @pytest.mark.order(3)
    def test_contactForm(self):
        self.commands.testContactForm()
    @pytest.mark.order(4)
    def test_failTest(self):
        self.commands.testFail()
