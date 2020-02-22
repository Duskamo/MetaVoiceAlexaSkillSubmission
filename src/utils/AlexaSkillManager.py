
import os
import json
import time
import subprocess

class AlexaSkillManager:
	def __init__(self,jsonDict):
		script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
		rel_creator_path = "../files/skill_creator"
		rel_creator_input_path = "../files/skill.json"
		rel_modifier_path = "../files/skill_modifier"
		rel_modifier_input_path = "../files/model.json"
		rel_submitter_path = "../files/skill_submitter"
		
		
		self.SKILL_CREATOR_BATCH = os.path.join(script_dir, rel_creator_path)
		self.SKILL_CREATOR_INPUT = os.path.join(script_dir, rel_creator_input_path)
		self.SKILL_MODIFIER_BATCH = os.path.join(script_dir, rel_modifier_path)
		self.SKILL_MODIFIER_INPUT = os.path.join(script_dir, rel_modifier_input_path)
		self.SKILL_SUBMITTER_BATCH = os.path.join(script_dir, rel_submitter_path)
		self.jsonDict = json.loads(jsonDict)


	def createAlexaSkill(self):
		cmd = "sudo " + self.SKILL_CREATOR_BATCH + " " + self.SKILL_CREATOR_INPUT 

		output = subprocess.check_output(cmd,shell=True)

		# Wait for request to complete
		time.sleep(10)

		for item in output.split("\n"):
			if "Skill ID:" in item:
				output = item.strip()
				output = output.replace("Skill ID: ", "")

		self.skillID = output


	def modifyAlexaSkill(self):
		cmd = "sudo " + self.SKILL_MODIFIER_BATCH + " " + self.skillID + " " + self.SKILL_MODIFIER_INPUT 

		subprocess.check_output(cmd,shell=True)

		# Wait for request to complete
		time.sleep(120)


	def submitAlexaSkill(self):
		cmd = "sudo " + self.SKILL_SUBMITTER_BATCH + " " + self.skillID

		subprocess.check_output(cmd,shell=True)
