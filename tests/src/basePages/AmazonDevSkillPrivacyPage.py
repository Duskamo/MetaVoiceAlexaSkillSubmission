
from src.utils.BasePage import *


class AmazonDevSkillPrivacyPage(BasePage):
    def __init__(self):
        super(AmazonDevSkillPrivacyPage, self).__init__()

    def setPrivacyInformation(self):
        self.privacyRadioButton1 = self.driver.find_element_by_xpath(".//*[@class='global-options']/edw-user-input[1]//*[@class='UpdateApplicationFormRowTextBox']/div[2]/span/span[2]//input")
        self.privacyRadioButton1.click()

        self.privacyRadioButton2 = self.driver.find_element_by_xpath(".//*[@class='global-options']/edw-user-input[2]//*[@class='UpdateApplicationFormRowTextBox']/div/span/span[2]//input")
        self.privacyRadioButton2.click()

        self.privacyRadioButton3 = self.driver.find_element_by_xpath(".//*[@class='global-options']/edw-user-input[3]//*[@class='UpdateApplicationFormRowTextBox']/div/span/span[2]//input")
        self.privacyRadioButton3.click()

        self.complianceRadioButton1 = self.driver.find_element_by_id("ExportComplianceCheckBox")
        self.complianceRadioButton1.click()

        self.complianceRadioButton2 = self.driver.find_element_by_xpath(".//*[@class='global-options']/edw-user-input[5]//*[@class='UpdateApplicationFormRowTextBox']/div/span/span[2]//input")
        self.complianceRadioButton2.click()

    def saveAndPublishAlexaSkill(self):
        self.saveButton = self.driver.find_element_by_id("edw-save-skill-button")
        self.saveButton.click()

        self.waitPageLoad()

        self.publishSkillButton = self.driver.find_element_by_id("edw-submit-for-certification-button")
        self.publishSkillButton.click()

        self.waitPageLoad()

        self.verificationAlertBoxYESButton = self.driver.find_element_by_xpath(".//*[@id='edw-message-box']/button[1]")
        self.verificationAlertBoxYESButton.click()

    def close(self):
        self.driver.close()