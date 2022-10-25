import os
import pytest
import allure
from selenium import webdriver as wd


# Set up
@pytest.fixture(params=['chrome', 'firefox'], scope='function')
def init_driver(request):
    if request.param == 'chrome':
        options = wd.ChromeOptions()
        driver = wd.Remote(
            command_executor=os.getenv('REMOTE_DRIVER_URL'),
            options=options)
    elif request.param == 'firefox':
        options = wd.FirefoxOptions()
        driver = wd.Remote(
            command_executor=os.getenv('REMOTE_DRIVER_URL'),
            options=options)

    request.cls.driver = driver
    driver.implicitly_wait(20)

    yield

    if request.node.rep_call.failed:
        try:
            with allure.step("Please see the below error screenshot for more information: "):
                allure.attach(driver.get_screenshot_as_png(), name=request.function.__name__, attachment_type=allure.
                              attachment_type.PNG)
        except Exception as e:
            print("Fail to take screen-shot: {}".format(e))

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(autouse=True, scope='session')
def setup_teardown():
    # setup
    yield
    # teardown
