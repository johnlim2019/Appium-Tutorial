import pytest
import unittest
from KWA_demo_commands import DemoCommands
import refLib


@pytest.mark.usefixtures('createClassDriver')
class test_KWA_Demo(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setupClassObject(self):
        self.commands = DemoCommands(self.driver,__file__)
        print('constructed commands obj')
    @pytest.mark.order(1)
    def test_Homepage(self):
        self.commands.testHomepage()
    @pytest.mark.order(2)    
    def test_EnterSomeValue(self):
        self.commands.testEnterSomeValue()

