import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
import time
from utilites.readProperties import ReadConfig
from utilites.customerLogger import LogGen

from selenium.webdriver.common.by import By
from utilites import ExcelUtils


class Test_002_ddl_Login:
    baseUrl = ReadConfig.getApplicationURL()
    path = ".//TestData/Testdata.xlsx"
    logger = LogGen.loggen()

    def test_002_ddl_login(self, setup):
        self.logger.info("**************************** test_002_ddl_login **********")
        self.logger.info("**************************** verifying Login ***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(3)
        self.lp = Loginpage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("number of Rows i a excel", self.rows)

        lst_status = []  # empty list
        for r in range(2, self.rows+1):
            self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Revinate Home"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("***************pased")
                    self.lp.clickMyacount()
                    time.sleep(4)
                    self.lp.clickLogout();
                    lst_status.append("Pass")

                elif self.exp=="Fail":
                    self.logger.info("*************** failed")
                    self.lp.clickMyacount()
                    time.sleep(4)
                    self.lp.clickLogout();
                    lst_status.append("Failed")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*************** failed")
                    self.lp.clickMyacount()
                    time.sleep(4)
                    self.lp.clickLogout();
                    lst_status.append("fail")
                elif self.exp == "Fail":
                    self.logger.info("*************** pass")
                    self.lp.clickMyacount()
                    time.sleep(4)
                    self.lp.clickLogout();
                    lst_status.append("pass")
        if "Fail" not in lst_status:
            self.logger.info("*********** login ddl test Pass ****")
            self.driver.close()
            assert True
        else:
            self.logger.info("*********** login ddl test Failed ****")
            self.driver.close()
            assert False
        self.logger.info("***************end of login ddt test **********")
        self.logger.info("****************** completed ***************");

