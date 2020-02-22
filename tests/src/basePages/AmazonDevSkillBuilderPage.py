
from src.utils.BasePage import *
from src.basePages.AmazonDevSkillConfigurationPage import *


class AmazonDevSkillBuilderPage(BasePage):
    def __init__(self):
        super(AmazonDevSkillBuilderPage, self).__init__()

    def addNewIntent(self,intents):
        # Click add intent button
        self.addIntentButton = self.driver.find_element_by_class_name("create-intent")
        self.addIntentButton.click()

        # Enter intent name
        self.intentNameTextField = self.driver.find_element_by_class_name("askui-input-full-size")
        self.intentNameTextField.send_keys(intents['intent'])

        # Click Create Intent button
        self.createIntentButton = self.driver.find_element_by_xpath(".//*[@class='custom-intent-input-wrapper']/button")
        self.createIntentButton.click()


    def addUtterances(self,utterances):
        self.utterancePlusSignButton = self.driver.find_element_by_xpath(".//*[@class='input-highlighter-create-item']/button")
        self.utteranceCreateTextField = self.driver.find_element_by_xpath(".//main//*[@class='input-highlighter-create-item']/div/div")

        for key, value in utterances.iteritems():
            self.utteranceCreateTextField.send_keys(value)
            self.wait(2)
            self.utterancePlusSignButton.click()


        self.waitPageLoad()

    def saveSkills(self):
        self.saveModelMenuItem = self.driver.find_element_by_xpath(".//*[@class='askui-toolbar-actions']/button[1]")
        self.saveModelMenuItem.click()

        self.waitPageLoad()

    def buildModel(self):
        self.buildModelMenuItem = self.driver.find_element_by_xpath(".//*[@class='askui-toolbar-actions']/button[2]")
        self.buildModelMenuItem.click()

        self.wait(120)

    def gotoSkillConfigurationPage(self):
        self.configurationNavMenuButton = self.driver.find_element_by_xpath(".//*[@class='askui-skill-navigation']/a[3]")
        self.configurationNavMenuButton.click()

        self.waitPageLoad()

        amazonDevSkillConfigurationPage = AmazonDevSkillConfigurationPage()
        amazonDevSkillConfigurationPage.driver = self.driver
        return amazonDevSkillConfigurationPage

    ## Helpers

    def wait(self,sec):
        time.sleep(sec)