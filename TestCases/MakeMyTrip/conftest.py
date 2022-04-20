import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from Utilities.filepath import *

@pytest.hookimpl(hookwrapper=True,tryfirst=True)
def pytest_runtest_makereport(item,call):

    outcome = yield
    rep = outcome.get_result()
    setattr(item,"rep_" + rep.when, rep)
    test_fn = item.obj
    docstring = getattr(test_fn, '__doc__')
    if docstring:
        rep.model = docstring
    return  rep

@pytest.fixture(scope="function")
def selenium_driver(request):
    chrome_options = Options()
    s = Service(FilePath.chromedriver_path)
    driver = webdriver.Chrome(service=s,options=chrome_options)
    url = "https://www.makemytrip.com/"
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    request.cls.driver=driver
    yield driver
    driver.close()



