
from src.utils.BasePage import *
from src.basePages.AmazonDevSkillsSkillInformationPage import *


class AmazonDevSkillsPage(BasePage):
    def __init__(self):
        super(AmazonDevSkillsPage, self).__init__()

    def gotoSkillInformationPage(self):
        addNewSkillButton = self.driver.find_element_by_xpath(".//*[@class='EDWHeaderContainer']/button")
        addNewSkillButton.click()

        amazonDevSkillsSkillInformationPage = AmazonDevSkillsSkillInformationPage()
        amazonDevSkillsSkillInformationPage.driver = self.driver
        return amazonDevSkillsSkillInformationPage