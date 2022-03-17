import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup():
    option = Options()
    driver = webdriver.Chrome(chrome_options=option, executable_path="C:/Users/TranInc/PycharmProjects/automation/drivers/chromedriver.exe")
    return driver

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'test'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'tuan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("python_HOME", None)
    metadata.pop("Plugins", None)