from refLib import OperationsFramework
import time
# the following Demo Class is inheriting/extending the OperationsFramework class
# DemoCommands is child of OperationsFramework
class DemoCommands(OperationsFramework):
    def __init__(self, driver,filename):
        super().__init__(driver,filename) 
        # call the super's init
        # when we create DemoCommands, we create an instance of the parent OperationsFramework
        # that Wraps the DemoCommands instance
        self.driver = driver
    # private attributes 
    _title = 'Appium Demo' 
    _imageClass = 'android.widget.ImageView'
    _zoomImageIndex = 0 
    _EnterSomeValue = 'ENTER SOME VALUE'
    _ContactUsForm = 'CONTACT US FORM'
    _ScrollView = 'ScrollView'
    _TabActivity ='Tab Activity'.upper()
    _Zoom = 'ZOOM'
    _Login = 'LOGIN'
    _LongClick ='LONG CLICK'
    _Time = 'TIME'
    _Date = 'DATE'
    _Pinch ='pinch in out'.upper()
    _DragAndDrop = 'DragAndDrop'.upper()
    _Crash = 'CRASH'
    _AutoSuggest = 'AUTO SUGGESTION'
    _SubmitBtn = 'SUBMIT'
    _sampleText = "I can't count the reasons I should stay. One by one they all begin to fade away."
    _sampleNumber = '12128937138'
    _noExisting = 'Blyat! Blin!'
    
    def testHomepage(self):
        assert self.isDisplayed(self._title) == True
    def testEnterSomeValue(self):
        self.clickElement(self._EnterSomeValue)
        self.isDisplayed('Enter some Value')
        self.sendText(self._sampleText,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText','xpath')        
        self.clickElement(self._SubmitBtn)
        self.getElement('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText','xpath').clear()
        assert self.isDisplayed(self._sampleText) == True
