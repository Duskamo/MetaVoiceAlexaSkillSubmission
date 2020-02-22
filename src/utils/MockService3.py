
class MockService3:
    def __init__(self):
        ""

    @staticmethod
    def getJson():
        return {
           "category":"Smart Home",
           "intents":[
              {
                 "intent":"intent",
                 "response":"gyu",
                 "utterances":{
                    "1":"Alexa gyu",
                    "3":"gyuq",
                    "2":"gyuw",
                    "5":"gyue",
                    "4":"gyur"
                 }
              }
           ],
           "skillName":"ygu",
           "firstName":"ftygu",
           "lastName":"yug",
           "longDescription":"gyu",
           "code":"def create_response(text, shouldEndSession):\n    return {\n        'version': '1.0',\n        'sessionAttributes': {},\n        'response': {\n          'outputSpeech': {\n              'type': 'PlainText',\n              'text': text\n          },\n          'card': {\n              'type': 'Simple',\n              'title': 'ygu',\n              'content': text\n          },\n          'reprompt': {\n              'outputSpeech': {\n                  'type': 'PlainText',\n                  'text': \"text\"\n              }\n          },\n          'shouldEndSession': shouldEndSession\n        }\n    }\n\n\ndef lambda_handler(event, context):\n\n    #on launch request prompt user to ask for help\n    if event['request']['type'] == 'LaunchRequest':\n        return create_response('If you dont know how to use me you can ask for help by saying help', False)\n\n    #give user utterances\n    elif event['request']['intent']['name'] == 'Help':\n        return create_response('There are several commands, try saying gyu', False)\n\n    #end session\n    elif event['request']['type'] == 'SessionEndedRequest':\n        return create_response('', True)\n\n    #end session\n    elif event['request']['intent']['name'] == 'endSession':\n        return create_response('', True)\n\n    #user defined intents\n    #paste content here\n    elif event['request']['intent']['name'] == 'intent':\n        return create_response('gyu', True)\n\n",
           "template":"Alexa Interaction",
           "invocationName":"gyu",
           "keywords":"gyu",
           "shortDescription":"gyu",
           "email":"gyu",
            "arn":"arn:aws:lambda:us-east-1:197224448158:function:rdt_trdy_yt"
        }