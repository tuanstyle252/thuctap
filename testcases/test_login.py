import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
import time
from utilites.readProperties import ReadConfig
from utilites.customerLogger import LogGen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("**************************** Test_001_Login **********************")
        self.logger.info("**************************** verifying Home Page Title ***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Log in to Revinate":
            assert True
            self.logger.info(" ******************************** Home Page is Test Passed************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error(" ******************************** Home Page is Test Failed *************")
            assert False

    def test_login(self, setup):
        self.logger.info("**************************** verifying Login ***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(3)
        self.lp=Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Revinate Home":
            assert True
            self.logger.info(" ******************************** login is Test Passed ************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error(" ******************************** login is Test Failed ************")
            assert False
    
    def test_logout(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(3)
        self.lp=Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.lp.clickMyacount()
        time.sleep(5)
        self.lp.clickLogout()
        time.sleep(4)
        act_title = self.driver.title
        if act_title == "Log in to Revinate":
            assert True
            self.logger.info("******************* lougout passed **********")
            self.driver.close()
        else:
            assert False
            self.logger.info("******************* lougout fail **********")
            self.driver.close()

    def test_forgot(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(3)
        self.lp=Loginpage(self.driver)
        time.sleep(2)
        self.lp.clickForgot()
        time.sleep(4)
        self.lp.clickemailforgotpassword(self.username)
        time.sleep(3)
        self.lp.submitforgot()
        self.driver.close()
