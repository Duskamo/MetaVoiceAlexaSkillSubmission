
import time
import json
import os
import fileinput
from shutil import copyfile

class TemplateHelper:
	def __init__(self,jsonDict):
		self.jsonDict = json.loads(jsonDict)

		script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
		rel_src_skill_path = "../files/skill_template.json"
		rel_dst_skill_path = "../files/skill.json"
		rel_src_model_path = "../files/model_template.json"
		rel_dst_model_path = "../files/model.json"

		self.SKILL_SRC = os.path.join(script_dir, rel_src_skill_path)
		self.SKILL_DST = os.path.join(script_dir, rel_dst_skill_path)
		self.MODEL_SRC = os.path.join(script_dir, rel_src_model_path)
		self.MODEL_DST = os.path.join(script_dir, rel_dst_model_path)

	def modifySkillTemplate(self):
		# Find all used items from dictrionary
		name = self.jsonDict["skillName"] + "_" + self.jsonDict["firstName"] + "_" + self.jsonDict["lastName"]

		# Create copy of skill_template file for prod purposes
		copyfile(self.SKILL_SRC,self.SKILL_DST)

		time.sleep(5)

		# Replace contents in newly created file with used items from dictionary
		r = open(self.SKILL_SRC,"r").read()
		s = open(self.SKILL_DST,"r+")

		r = r.replace('{0}', self.jsonDict["shortDescription"])
		r = r.replace('{1}', self.jsonDict["intents"][0]["utterances"]["1"])
		r = r.replace('{2}', self.jsonDict["intents"][0]["utterances"]["2"])
		r = r.replace('{3}', self.jsonDict["intents"][0]["utterances"]["3"])
		r = r.replace('{4}', name)
		r = r.replace('{5}', self.jsonDict["longDescription"])
		#r = r.replace('{6}', self.jsonDict["category"])
		r = r.replace('{6}', "SMART_HOME")
		r = r.replace('{7}', self.jsonDict["arn"])

		s.write(r)
	
		s.close()

	def modifyModelTemplate(self):
		# Find all used items from dictrionary
		name = self.jsonDict["skillName"] + "_" + self.jsonDict["firstName"] + "_" + self.jsonDict["lastName"]

		print(self.jsonDict["invocationName"])
		print(self.jsonDict["intents"][0]["intent"])
		print(self.jsonDict["intents"][0]["utterances"]["1"])
		print(self.jsonDict["intents"][0]["utterances"]["2"])
		print(self.jsonDict["intents"][0]["utterances"]["3"])
		print(self.jsonDict["intents"][0]["utterances"]["4"])
		print(self.jsonDict["intents"][0]["utterances"]["5"])

		# Create copy of skill_template file for prod purposes
		copyfile(self.MODEL_SRC,self.MODEL_DST)
		
		time.sleep(5)
		
		# Replace contents in newly created file with used items from dictionary
		r = open(self.MODEL_SRC,"r").read()
		s = open(self.MODEL_DST,"r+")

		r = r.replace('{0}', self.jsonDict["invocationName"])
		r = r.replace('{1}', self.jsonDict["intents"][0]["intent"])
		r = r.replace('{2}', self.jsonDict["intents"][0]["utterances"]["1"])
		r = r.replace('{3}', self.jsonDict["intents"][0]["utterances"]["2"])
		r = r.replace('{4}', self.jsonDict["intents"][0]["utterances"]["3"])
		r = r.replace('{5}', self.jsonDict["intents"][0]["utterances"]["4"])
		r = r.replace('{6}', self.jsonDict["intents"][0]["utterances"]["5"])

		s.write(r)
	
		s.close()
		






