import pytest
import time
import refLib
import KWA_demo_commands
@pytest.fixture(scope='class')
def createClassDriver(request):
    print('Before Class')
    driver = refLib.getDriver()
    if request.cls is not None: # we create in the test class the driver attribute holding the driver object
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')

# fixtures 
# these are statically declared variables and instances that will be used by 
# all tests within the scope 
# they provide a consistent context for the running of each tests
# 