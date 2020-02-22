
from src.utils.BasePage import *
from src.basePages.AmazonDevSkillInteractionModelPage import *


class AmazonDevSkillsSkillInformationPage(BasePage):
    def __init__(self):
        super(AmazonDevSkillsSkillInformationPage, self).__init__()

    def fillSkillInformation(self,json):
        appName = str(json['firstName']) + "_" + str(json["lastName"]) + "_" + str(json["skillName"])

        self.nameTextBox = self.driver.find_element_by_xpath(".//*[@class='AppManagementFormsBox']/div/div/edw-user-input[3]//input")
        self.nameTextBox.send_keys(appName)

        self.invocationNameTextBox = self.driver.find_element_by_xpath(".//*[@class='AppManagementFormsBox']/div/div/edw-user-input[4]//input")
        self.invocationNameTextBox.send_keys(json['invocationName'])

    def saveSkillInformation(self):
        self.saveSkillButton = self.driver.find_element_by_id("edw-save-skill-button")
        self.saveSkillButton.click()

        self.waitPageLoad()

    def gotoInteractionModelPage(self):
        self.submitButton = self.driver.find_element_by_id("edw-next-skill-tab-button")
        self.submitButton.click()

        amazonDevSkillInteractionModelPage = AmazonDevSkillInteractionModelPage()
        amazonDevSkillInteractionModelPage.driver = self.driver
        return amazonDevSkillInteractionModelPage