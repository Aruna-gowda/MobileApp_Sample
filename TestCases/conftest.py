from appium import webdriver
import allure
import pytest
from allure_commons.types import AttachmentType
from appium.options.common.base import AppiumOptions
from Utilities import ReadConfigurations

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test",attachment_type=AttachmentType.PNG)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture()
def setup_and_teardown(request):
    url = ReadConfigurations.read_configuration("basic info", "url")
    platformName = ReadConfigurations.read_configuration("basic info","platformName")

    global driver
    driver = None

    if platformName == "Android":
        options = AppiumOptions()
        options.load_capabilities({
            "platformName": "Android",
            "appium:deviceName": "emulator-5554",
            "appium:automationName": "UiAutomator2",
            "appium:platformVersion": "14",
            "appium:app": "C:/Users/Aruna Aruna/Downloads/app.apk",
            "appium:appPackage": "ai.edify.rome.stg",
            "appium:appActivity": "ai.edify.rome.MainActivity",

            # "appium:app": "/Users/aruna/Downloads/app-release.apk",
            # "appium:appPackage": "app.aldar.live",
            # "appium:appActivityy": "app.aldar.live.MainActivity",
            "noReset": False,
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True
        })
        driver = webdriver.Remote(url, options=options)
        print("check whether device is locked or not :", driver.is_locked())
        print("Current Package", driver.current_package)
        print("Current Activity", driver.current_activity)
        print("Current context", driver.current_context)
    elif platformName == "iOS":
        options = AppiumOptions()
        options.load_capabilities({
            "platformName": "iOS",
            "appium:deviceName": "iPhone 12",
            "appium:automationName": "XCUITest",
            "appium:platformVersion": "16",
            "appium:app": "path of the ipa file",
            "appium:appPackage": "app.aldar.live",
            "appium:appActivityy": "app.aldar.live.MainActivity",
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 600,
            "appium:connectHardwareKeyboard": True,
            "noReset": True
        })
        driver = webdriver.Remote(url, options=options)
    else:
        print("No device found for the option you have chosen. Please chose an aoption between 'android or iOS")

    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()
