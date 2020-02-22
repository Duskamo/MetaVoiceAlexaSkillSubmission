
from src.utils.BasePage import *
from src.basePages.AmazonDevSkillPublishingPage import *


class AmazonDevSkillConfigurationPage(BasePage):
    def __init__(self):
        super(AmazonDevSkillConfigurationPage, self).__init__()

    def configureARN(self,arn):
        # Select AWS Lambda RadioButton
        self.awsLambdaRadioButton = self.driver.find_element_by_id("service-endpoint-lambda")
        self.awsLambdaRadioButton.click()

        # Enter ARN into text field
        self.arnTextField = self.driver.find_element_by_xpath(".//*[@class='AppManagementFormsBox']//*[@ng-init='edwInit']")
        self.arnTextField.send_keys(arn)

        self.waitPageLoad()

    def saveConfiguration(self):
        self.saveConfigButton = self.driver.find_element_by_id("edw-save-skill-button")
        self.saveConfigButton.click()

        self.waitPageLoad()

    def gotoSkillPublishingPage(self):
        self.configNextButton = self.driver.find_element_by_id("edw-next-skill-tab-button")
        self.configNextButton.click()

        self.waitPageLoad()

        self.testNextButton = self.driver.find_element_by_id("edw-next-skill-tab-button")
        self.testNextButton.click()

        amazonDevSkillPublishingPage = AmazonDevSkillPublishingPage()
        amazonDevSkillPublishingPage.driver = self.driver
        return amazonDevSkillPublishingPage