
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
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	options.add_argument('--disable-extensions')
	options.add_argument('--disable-gpu')
	options.add_argument('--no-sandbox')
	self.driver = webdriver.Chrome('usr/local/bin/chromedriver',chrome_options=options)
	self.driver.maximize_window()
	self.driver.get(self.url)
	"""
	
	options = Options()
	options.add_argument('--headless')
	self.driver = webdriver.Firefox(firefox_options=options,executable_path='/usr/local/bin/geckodriver')
	self.driver.maximize_window()
        self.driver.get(self.url)
        

    def login(self,email,password):
	self.waitPageLoad()
        usernameTextField = self.driver.find_element_by_xpath(".//*[@id='ap_email']")
	usernameTextField.send_keys(email)
        self.waitPageLoad()
        passwordTextField = self.driver.find_element_by_xpath(".//*[@id='ap_password']")
	passwordTextField.send_keys(password)
        self.waitPageLoad()
        print("Page 1: " + self.driver.current_url)


        loginButton = self.driver.find_element_by_xpath(".//*[@id='signInSubmit']")
        self.waitPageLoad()

        print("Login Button Text: " + loginButton.text)
        print("Username TF: " + usernameTextField.text)
        print("Password TF: " + passwordTextField.text)

        loginButton.click()
        self.waitPageLoad()
        print("Page 2: " + self.driver.current_url)
        print("Email: " + email)
        print("Password: " + password)
        
        amazonDevConsoleDashboardPage = AmazonDevConsoleDashboardPage()
        amazonDevConsoleDashboardPage.driver = self.driver
        return amazonDevConsoleDashboardPage
