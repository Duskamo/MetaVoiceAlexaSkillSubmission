
from src.utils.BasePage import *
from src.basePages.AmazonDevSkillPrivacyPage import *


class AmazonDevSkillPublishingPage(BasePage):
    def __init__(self):
        super(AmazonDevSkillPublishingPage, self).__init__()

    def setPublishingCategory(self,category):
        self.publishingCategorySelectorItem = self.driver.find_element_by_xpath(".//option[@label='{}']".format(category))
        self.publishingCategorySelectorItem.click()

    def setPublishingInformation(self,json):
        self.testingInstructionsTextArea = self.driver.find_element_by_xpath(".//*[@class='AppManagementFormsBox']/div/div/div//textarea[1]")
        self.testingInstructionsTextArea.send_keys(json['category'] + " - " + json['shortDescription'])

        self.shortDescriptionTextArea = self.driver.find_element_by_xpath(".//*[@class='AppManagementFormsBox']/div/div/edw-user-input[1]//textarea")
        self.shortDescriptionTextArea.send_keys(json['shortDescription'])

        self.fullDescriptionTextArea = self.driver.find_element_by_xpath(".//*[@class='AppManagementFormsBox']/div/div/edw-user-input[2]//textarea")
        self.fullDescriptionTextArea.send_keys(json['longDescription'])


        if json['intents'][0]['utterances']["1"] is not None:
            self.examplePhrasesTextField1 = self.driver.find_element_by_xpath(".//*[@id='examplePhraseList']/li[1]/input")
            self.examplePhrasesTextField1.send_keys(json['intents'][0]['utterances']["1"])


        if json['intents'][0]['utterances']["2"] is not None:
            self.examplePhrasesTextField2 = self.driver.find_element_by_xpath(".//*[@id='examplePhraseList']/li[2]/input")
            self.examplePhrasesTextField2.send_keys(json['intents'][0]['utterances']["2"])


        if json['intents'][0]['utterances']["3"] is not None:
            self.examplePhrasesTextField2 = self.driver.find_element_by_xpath(".//*[@id='examplePhraseList']/li[3]/input")
            self.examplePhrasesTextField2.send_keys(json['intents'][0]['utterances']["3"])

        self.waitPageLoad()

    def setImages(self):
        self.smallIconImage = self.driver.find_element_by_xpath(".//*[@id='edw-presentation-iconUploader']//input")
        self.smallIconImage.send_keys("/var/www/html/bluemarble_workspace/MetaVoiceAlexaSkillSubmission/media/bluemarble_icon_108.png")

        self.waitPageLoad()

        self.largeIconImage = self.driver.find_element_by_xpath(".//*[@class='AppManagementFormsBox']/div/div/edw-user-input[5]//input")
        self.largeIconImage.send_keys("/var/www/html/bluemarble_workspace/MetaVoiceAlexaSkillSubmission/media/bluemarble_icon_512.png")

        self.waitPageLoad()

    def saveInformation(self):
        self.saveButton = self.driver.find_element_by_id("edw-save-skill-button")
        self.saveButton.click()

        self.waitPageLoad()

    def gotoSkillPrivacyPage(self):
        self.nextButton = self.driver.find_element_by_id("edw-next-skill-tab-button")
        self.nextButton.click()

        self.waitPageLoad()

        amazonDevSkillPrivacyPage = AmazonDevSkillPrivacyPage()
        amazonDevSkillPrivacyPage.driver = self.driver
        return amazonDevSkillPrivacyPage
