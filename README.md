# Appium-Tutorial
 
## python libraries 
* pip install pytest
* pip install pytest-order
* pip install qase-pytest
* pip install pytest-only

## How to return an appium element locator
* We can identify an element and return as a variable
* with this variable we can conduct assertions on its attributes without losing the element. 
* this variable will break when we change activity as the screen will rerender the app's xml py

## saving images on test failure (NOT USED)
* under the pytest file
* in the pytest class, create a variable to be used to check fail
```python
@pytest.mark.usefixtures('createClassDriver')
class test_KWA_Demo(unittest.TestCase):
    test_failed = None
```
* in the `tearDown()`, part of `unittest` library which is part of the core python libraries, of the fixture that setup each test, check the `test_failed` and if `true` save an image and attach it to allure
* we also take the opportunity to reset any actions taken by the previous test, in this case it would be to return to the homepage
```python
def tearDown(self):
# if fail take screenshot
if self.test_failed:
    imageFile = self.commands.screenShot('test_KWA_demo_fail')
    allure.attach.file(imageFile, attachment_type=allure.attachment_type.PNG)
    self.test_failed = False
# if we are not at the homepage, go back, check by looking for the title after scrolling to the top
self.commands.scrollUp(3000)
if self.commands.isDisplayed('Appium Demo') != True:
    self.commands.systemBackBtn()
```

### Screenshot errors
* In refLib, there are some functions that have try-except blocks
* these are getElement() and getElementFromElements() and clickElement() and sendText()
* most of the functions that do not have such as hasAttribute and isDisplayed do not take screenshot, as we can have negative assertions that element does not have attribute or is not displayed. 
* But the assertions are not impacted.
* using try-except blocks, if the calling function is not able to find the element we will take a screenshot and send it to both allure and qase


## using Allure
* allure will generate a log file that can be used to generate a dashboard 
* the log file contains for each tests, the logs that our logger makes, so it allows for some debugging. 
* we can also attach png when a test fails
* create the allure logs
  * `py.test --alluredir='C:\SUTD-ONEDRIVE\internshit\appium\Appium-Tutorial\allureLogs' -s -v`
* generate the dashboard
  * `allure serve 'C:\SUTD-ONEDRIVE\internshit\appium\Appium-Tutorial\allureLogs'`

## Allure steps
* in order to show the steps for each test, use `allureSteps(test descriptions)` function 
* steps are accurately displayed


## using qase 
* create a new testrun based on test plan 
* Appium Tutorial api = `8a8bf109ed59fc925b49d7328d1aeaf96143c128`
* ProjectCode = `AT`
* To create a new automated test

## qase steps
* `use reportSteps(test descriptions)`
* the reporting of steps is intermittent and not reliable.

## combined qase and allure command
`py.test --qase-mode=testops --qase-to-api-token=8a8bf109ed59fc925b49d7328d1aeaf96143c128 --qase-to-project=AT --alluredir='C:\SUTD-ONEDRIVE\internshit\appium\Appium-Tutorial\allureLogs' -s -v`
```
pytest \
    --qase-mode=testops \
    --qase-to-api-token=<your api token here> \
    --qase-to-project=PRJCODE \ # project, where your testrun exists in
    --qase-to-plan=1 # testplan id
```
### Qase-to-plan seems to be broken, qase-to-run too is broken


