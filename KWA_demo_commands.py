from refLib import OperationsFramework, allureSteps, reportSteps
from qaseio.pytest import qase
import time
# the following Demo Class is inheriting/extending the OperationsFramework class
# DemoCommands is child of OperationsFramework


class DemoCommands(OperationsFramework):
    def __init__(self, driver, filename):
        super().__init__(driver, filename)
        # call the super's init
        # when we create DemoCommands, we create an instance of the parent OperationsFramework
        # that Wraps the DemoCommands instance
        self.driver = driver
    # private attributes
    _title = 'Appium Demo'
    _zoomImageIndex = 0
    _EnterSomeValue = 'ENTER SOME VALUE'
    _ContactUsForm = 'CONTACT US FORM'
    _ScrollView = 'ScrollView'
    _TabActivity = 'Tab Activity'.upper()
    _Zoom = 'ZOOM'
    _Login = 'LOGIN'
    _LongClick = 'LONG CLICK'
    _Time = 'TIME'
    _Date = 'DATE'
    _Pinch = 'pinch in out'.upper()
    _DragAndDrop = 'DragAndDrop'.upper()
    _Crash = 'CRASH'
    _AutoSuggest = 'AUTO SUGGESTION'
    _SubmitBtn = 'SUBMIT'
    _sampleText = "I can't count the reasons I should stay. One by one they all begin to fade away."
    _sampleNumber = '12128937138'
    _noExisting = 'Blyat! Blin!'
    _sampleName = 'Hugo'
    _sampleEmail = '@mail'
    _sampleAddress = "19 Idiot's Lane, Dumb City"

    def testHomepage(self):
        assert self.isDisplayed(self._title) == True
        reportSteps('Found Title')
        allureSteps('Found Title')
        image = self.getElementFromElements('android.widget.ImageView', 'class', 0)
        assert image.is_displayed()
        reportSteps('Found Image')
        allureSteps('Found Image')        
        self.clickElement(self._EnterSomeValue)

    def testEnterSomeValue(self):
        self.clickElement(self._EnterSomeValue)
        assert self.isDisplayed('Enter some Value') == True
        reportSteps('Found "Enter some Value" title')
        allureSteps('Found "Enter some Value" title')
        input = self.getElementFromElements('android.widget.EditText', 'class', 0)
        input.send_keys(self._sampleText)
        self.clickElement(self._SubmitBtn)
        input.clear()
        preview = self.getElementFromElements('android.widget.TextView', 'class', -1)
        assert self.hasAttribute(element=preview, attribute='text', expectedValue=self._sampleText) == True
        reportSteps('Successful submission of text')
        allureSteps('Successful submission of text')

    def testContactForm(self):
        self.hasAttribute('CONTACT US FORM', 'text', locatorValue='4', locatorType='index')
        self.clickElement(self._ContactUsForm)
        self.hasAttribute('CONTACT US FORM', 'text', locatorValue='0', locatorType='index')
        self.sendText(self._sampleName, 'Enter Name')
        self.sendText(self._sampleEmail, 'Enter Email')
        self.sendText(self._sampleAddress, 'Enter Address')
        self.sendText(self._sampleNumber, 'Enter Mobile No')
        self.clickElement('SUBMIT')
        assert self.hasAttribute(self._sampleName, 'text', '6', 'index') == True
        reportSteps('Name Field Works')
        allureSteps('Name Field Works')
        assert self.hasAttribute(self._sampleEmail, 'text', '7', 'index') == True
        reportSteps('Email Field Works')
        allureSteps('Email Field Works')
        assert self.hasAttribute(self._sampleAddress, 'text', '8', 'index') == True
        reportSteps('Address Field Works')        
        allureSteps('Address Field Works')        
        assert self.hasAttribute(self._sampleNumber, 'text', '9', 'index') == True
        reportSteps('Ph. Num Field Works')
        allureSteps('Ph. Num Field Works')
        
    def testFailGetElement(self):
        assert self.getElement(self._AutoSuggest) != None

    def testFailGetElementFromElements(self):
        assert self.getElementFromElements('android.widget.TextView','class',123) != None
        