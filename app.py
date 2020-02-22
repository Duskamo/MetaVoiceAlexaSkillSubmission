from flask import Flask, session, redirect, url_for, escape, request, render_template
import os
from src.helpers.TemplateHelper import *
from src.utils.AlexaSkillManager import *

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>welcome</h1>'

#simple post request to get json data from service 3
@app.route('/post', methods = ['POST'])
def get_post_json_data():

	#load the json
	jsonDict = request.get_json(silent=True)

	# Just for temporary logging purposes
	#print(jsonDict)

	# Populate Skill and Model json template files with user information
	templateHelper = TemplateHelper(jsonDict)
	templateHelper.modifySkillTemplate()
	templateHelper.modifyModelTemplate()

	# Create, modify, and submit new alexa skill for verification
	alexaSkillManager = AlexaSkillManager(jsonDict)
	alexaSkillManager.createAlexaSkill()
	alexaSkillManager.modifyAlexaSkill()
	alexaSkillManager.submitAlexaSkill()

	#print("Service 4 finished")

	return jsonDict

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5003.
	port = int(os.environ.get('PORT', 5003))
	app.run(host='0.0.0.0', port=port)
