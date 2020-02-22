
from src.utils.AlexaSkillAutomator import *
from src.utils.MockService3 import *

json = MockService3.getJson()
alexaSkillAutomator = AlexaSkillAutomator(json)
alexaSkillAutomator.automateTasks()
