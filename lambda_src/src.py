import random

"""
Simple Python Lambda function to realy a positive task to perform...
Intents supported:
    Open
    GetHelp
    Stop
    DoGood
    
"""

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(card_title, card_content, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': output
        },
        'card': {
            'type': 'Simple',
            'title': card_title,
            'content': card_content
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Your functions to implement your intents ------------------
ANODE_ACTIONS = {
    "Hold the door open for someone today.": "<speak>Hold the door open for someone today.</speak>",
    "Give someone a compliment.": "<speak>Give someone a compliment.</speak>",
    "Get your body moving. Do some form of exercise!": "<speak>Get your body moving. Whatever you are able to do just get moving! From jumping jacks to yard work. Whatever you decide, Exercising can help offset depression, anxiety, and stress.</speak>",
    "Listen to or read a positive or uplifting message": "<speak>Listen or read a positive message, or has uplifting content. The variety of subject matter, the better.</speak>",
    "Eat some veggies today!": "<speak>Eat a serving of at least two veggies today</speak>",
    "Thank a person that has helped you.": "<speak>Think about how a person has helped you in some way. This could either be a friend, family member, colleague, teacher, or even a pet. And go ahead and thank them. This can go a long way in making another feel good.</speak>",
    "Take a cold shower!": "<speak>Take a cold shower. Yes. Cold. Studies show, taking a cold shower can increase oxygen intake, alertness, and overall physical and mental wellness. One study showed, routine showers can help treat symptoms of depression. Go ahead. Jump in!</speak>",
    "Think about your life goals today, and everyday. Practice in thought, makes perfect.":"<speak>Think about your life goals. Do this not only after listening to my speech output, but everyday. Just like practice, if you follow a simple pattern, you can achieve what you want.</speak>",
    "Complete the most important thing on your to-do list.": "<speak>Complete the most important thing on your to do list.",
    "Stretch! Hold your stretch for 30 seconds!": "<speak>Stretch. Take a moment to stretch. Hold that stretch for at least thirty seconds. This will increase blood flow and oxygen intake. Which are good things. I would stretch myself, but alas. I am only hardware and software.</speak>",
    "Take a deep breath. Exhale for twice as long as it took you to inhale your breath.": "<speak>Take a deep breath. Hold it for ten seconds. Then exhale for twice the amount you inhaled.</speak>"
    }

# Having as variables (below) returns the same results each time,
# Though the card and speech output are the same pull.

# Try using conditions -->
# if speech_value = ANODE_ACTIONS[value0]
#   card_value = ANODE_ACTIONS[key0]

#card_key = random.choice(ANODE_ACTIONS.keys())
#speech_value = random.choice(ANODE_ACTIONS.values())

def anode_action(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True

    card_output = "" + card_key
    speech_output = speech_value

    return build_response(session_attributes, build_speechlet_response
                          ("Here's your Positive Tip", card_output, speech_output, reprompt_text, should_end_session))

                          
def stop(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True
    
    card_output = "Think positive! Have a nice day!"
    speech_output = "<speak>Thank you for asking Do Positive. Have a nice day!</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Session Ended", card_output, speech_output, reprompt_text, should_end_session))
                          

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for asking Do Positive."
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# --------------- Primary Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    logger.info("on_session_started requestId=" + session_started_request['requestId'] +
                ", sessionId=" + session['sessionId'])
                

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    logger.info("on_launch requestId=" + launch_request['requestId'] +
                ", sessionId=" + session['sessionId'])
    
    # Dispatch to skill's launch
    return build_response({},build_speechlet_response(
        "Do Positive", "Welcome to the Amazon Alexa skill, Do Positive!", "<speak>Welcome to the Amazon Alexa skill, Do Positive. I'll give you a suggestion to do something positive to help you or someone around you think positive! Just ask me for a Positive Action.</speak>","",False))


def get_help(intent, session):
    """ Called when the user asks for help """
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = False
    
    card_output = "Just ask: Give me a positive action or task "
    speech_output = "<speak>Ask for or tell me to say a positive action. And I'll suggest a positive task for you.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("What to Ask", card_output, speech_output, reprompt_text, should_end_session))


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    logger.info("on_intent requestId=" + intent_request['requestId'] +
                ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to skill's intent handlers

    if intent_name == "DoGood":
        return anode_action(intent, session)
    elif intent_name == "Stop":
        return stop(intent, session)
    elif intent_name == "GetHelp":
        return get_help(intent, session)
#    elif intent_name == "AMAZON.HelpIntent":
#        return get_help()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    logger.info("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    else:
        return on_session_ended(event['request'], event['session'])
