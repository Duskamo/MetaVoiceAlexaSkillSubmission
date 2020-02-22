
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from src.utils.BasePage import *
from src.basePages.AmazonDevConsoleDashboardPage import *

class AmazonDevLoginPage(BasePage):
    def __init__(self):
        super(AmazonDevLoginPage,self).__init__()
        self.url = "https://developer.amazon.com/home.html"

    def open(self):
        """
        firefoxOptions = Options()
        firefoxOptions.add_argument("--headless")
        self.driver = webdriver.Firefox(options=firefoxOptions, executable_path='/usr/local/bin/geckodriver')
        #self.driver.maximize_window()
        self.driver.get(self.url)
        """
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=options)
        self.driver.maximize_window()
        self.driver.get(self.url)
        


    def login(self,email,password):
        usernameTextField = self.driver.find_element_by_id("ap_email")
        usernameTextField.send_keys(email)

        passwordTextField = self.driver.find_element_by_id("ap_password")
        passwordTextField.send_keys(password)

        loginButton = self.driver.find_element_by_id("signInSubmit")
        loginButton.click()

        amazonDevConsoleDashboardPage = AmazonDevConsoleDashboardPage()
        amazonDevConsoleDashboardPage.driver = self.driver
        return amazonDevConsoleDashboardPage
