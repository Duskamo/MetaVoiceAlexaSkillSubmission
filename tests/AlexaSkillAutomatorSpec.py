
import unittest

from src.utils.AlexaSkillAutomator import *
from src.utils.MockService3 import *


class AlexaSkillAutomatorSpec(unittest.TestCase):
    def setUp(self):
        json = MockService3.getJson()
        self.alexaSkillAutomator = AlexaSkillAutomator(json)

    def tearDown(self):
        self.alexaSkillAutomator = None

    def test_FullAlexaSkillAutomation(self):
        self.alexaSkillAutomator.automateTasks()