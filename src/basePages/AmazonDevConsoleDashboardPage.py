
from src.utils.BasePage import *
from src.basePages.AmazonDevConsoleAlexaPage import *


class AmazonDevConsoleDashboardPage(BasePage):
    def __init__(self):
        super(AmazonDevConsoleDashboardPage,self).__init__()

    def gotoAlexaConsolePage(self):
        self.waitPageLoad()
        print(self.driver.current_url)

        self.driver.execute_script("arguments[0].scrollIntoView();",  self.driver.find_element_by_xpath(".//*[@id='top_nav_echodeveloperwebsite']"))
        alexaMenuItem = self.driver.find_element_by_xpath(".//*[@id='top_nav_echodeveloperwebsite']")

        alexaMenuItem.click()

        amazonDevConsoleAlexaPage = AmazonDevConsoleAlexaPage()
        amazonDevConsoleAlexaPage.driver = self.driver
        return amazonDevConsoleAlexaPage
