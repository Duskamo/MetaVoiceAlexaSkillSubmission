
from src.utils.BasePage import *
from src.basePages.AmazonDevSkillBuilderPage import *


class AmazonDevSkillInteractionModelPage(BasePage):
    def __init__(self):
        super(AmazonDevSkillInteractionModelPage, self).__init__()

    def openSkillBuilder(self):
        self.launchSkillBuilderButton = self.driver.find_element_by_xpath(".//*[@class='AppManagementFormsBox']//button")
        self.launchSkillBuilderButton.click()

        amazonDevSkillBuilderPage = AmazonDevSkillBuilderPage()
        amazonDevSkillBuilderPage.driver = self.driver
        return amazonDevSkillBuilderPage
