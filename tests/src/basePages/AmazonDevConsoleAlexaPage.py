
from src.utils.BasePage import *
from src.basePages.AmazonDevSkillsPage import *


class AmazonDevConsoleAlexaPage(BasePage):
    def __init__(self):
        super(AmazonDevConsoleAlexaPage, self).__init__()

    def gotoAlexaSkillsPage(self):
        alexaSkillKitButton = self.driver.find_element_by_xpath(".//*[@class='EDWHomeToolFrame']/div[2]/button")
        alexaSkillKitButton.click()

        amazonDevSkillsPage = AmazonDevSkillsPage()
        amazonDevSkillsPage.driver = self.driver
        return amazonDevSkillsPage