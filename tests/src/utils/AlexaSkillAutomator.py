import json
from selenium import webdriver

from src.basePages.AmazonDevLoginPage import *

class AlexaSkillAutomator:
    def __init__(self,jsonDict):
        #self.json = json.loads(jsonDict)
        self.json = jsonDict

    def automateTasks(self):
        email = "joe@xpollin.com"
        password = "Meta!!Voice!!2018!!"

        amazonDevLoginPage = AmazonDevLoginPage()
        amazonDevLoginPage.open()
        amazonDevLoginPage.waitPageLoad()

        amazonDevConsoleDashboardPage = amazonDevLoginPage.login(email,password)
        amazonDevConsoleDashboardPage.waitPageLoad()

        amazonDevConsoleAlexaPage = amazonDevConsoleDashboardPage.gotoAlexaConsolePage()
        amazonDevConsoleAlexaPage.waitPageLoad()

        amazonDevSkillsPage = amazonDevConsoleAlexaPage.gotoAlexaSkillsPage()
        amazonDevSkillsPage.waitPageLoad()

        amazonDevSkillsSkillInformationPage = amazonDevSkillsPage.gotoSkillInformationPage()
        amazonDevSkillsSkillInformationPage.waitPageLoad()
        amazonDevSkillsSkillInformationPage.fillSkillInformation(self.json)
        amazonDevSkillsSkillInformationPage.saveSkillInformation()

        amazonDevInteractionModelPage = amazonDevSkillsSkillInformationPage.gotoInteractionModelPage()
        amazonDevInteractionModelPage.waitPageLoad()

        amazonDevSkillBuilderPage = amazonDevInteractionModelPage.openSkillBuilder()

        amazonDevSkillBuilderPage.waitPageLoad()
        amazonDevSkillBuilderPage.addNewIntent(self.json['intents'][0])
        amazonDevSkillBuilderPage.addUtterances(self.json['intents'][0]['utterances'])
        amazonDevSkillBuilderPage.saveSkills()
        amazonDevSkillBuilderPage.buildModel()

        amazonDevSkillConfigurationPage = amazonDevSkillBuilderPage.gotoSkillConfigurationPage()
        amazonDevSkillConfigurationPage.waitPageLoad()
        amazonDevSkillConfigurationPage.configureARN(self.json['arn'])
        amazonDevSkillConfigurationPage.saveConfiguration()

        amazonDevSkillPublishingPage = amazonDevSkillConfigurationPage.gotoSkillPublishingPage()
        amazonDevSkillPublishingPage.waitPageLoad()
        amazonDevSkillPublishingPage.setPublishingCategory(self.json['category'])
        amazonDevSkillPublishingPage.setPublishingInformation(self.json)
        amazonDevSkillPublishingPage.setImages()
        amazonDevSkillPublishingPage.saveInformation()

        amazonDevSkillPrivacyPage = amazonDevSkillPublishingPage.gotoSkillPrivacyPage()
        amazonDevSkillPrivacyPage.waitPageLoad()
        amazonDevSkillPrivacyPage.setPrivacyInformation()
        amazonDevSkillPrivacyPage.saveAndPublishAlexaSkill()
        amazonDevSkillPrivacyPage.close()
