from selenium.webdriver.common.by import By


class Loginpage:
    textbox_username_xpath = "//input[@name = 'email']"
    textbox_password_xpath = "//input[@name = 'password']"
    button_login_xpath = "//button[@type = 'submit']"
    link_logout_xpath = '//*[@id="root"]/div[2]/header/div/div/ul/li[3]/ul/li[2]/a'
    link_myacount_logout = "//*[@id='root']/div[2]/header/div/div/ul/li[3]/a/i"


    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickMyacount(self):
        self.driver.find_element(By.XPATH, self.link_myacount_logout).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()

    def clickForgot(self):
        self.driver.find_element(By.XPATH, self.button_forgot_xpath).click()



