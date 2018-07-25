from __future__ import print_function

CardTitlePrefix = "Tech Hub"


# --------------- Helpers that build all of the responses ----------------------
def build_speechlet_response(title, output, reprompt_text, should_end_session):
    """
    Build a speechlet JSON representation of the title, output text, 
    reprompt text & end of session
    """
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': CardTitlePrefix + " - " + title,
            'content': output
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
    """
    Build the full response JSON from the speechlet response
    """
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

#
#                TODO
# 1) stop it from saying "there are one screen"
# 2) improve all dialogue
#
#

def sing(string):
    # ===========================
    # Converts plural to singular
    # ===========================
    import inflect
    words = string.split(' ')
    lastWord = words.pop(len(words) - 1)
    p = inflect.engine()
    output = p.singular_noun(lastWord)
    if output:
        return ' '.join(words + [output])
    else:
        return ' '.join(words + [lastWord])


def plu(string, count=2):
    # ===========================
    # Converts singular to plural
    # if the count is greater tha
    # n one.
    # ===========================
    import inflect
    p = inflect.engine()
    return p.plural(string, count)


# --------------- Functions that control the skill's behavior ------------------


def get_welcome_response():
    session_attributes = {}
    card_title = "Hello and welcome"
    speech_output = "Welcome to the Tech Hub. How can I help you?"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.

    reprompt_text = "I'm sorry - I didn't understand. How can I help you?"
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def explanation():
    """
    explains what the tech hub is
    """
    card_title = "Welcome to the Tech hub"
    speech_text = "The Tech Hub is a place of innovation. " + "We believe that technology is worth sharing, which is why we explore new ways to use emerging tech. " + "Current projects include developing skills for Alexa and Amazon Deep-lens, as well as using " + "rasberry pies in creative experiments. Tweet, us at hash tag Tech-Hub."
    return build_response({}, build_speechlet_response(card_title, speech_text, reprompt_text, False))


def functions():
    """
    explains what the tech hub skill can do
    """
    card_title = "Welcome to the Tech hub"
    speech_text = "Hello. I can tell you about the Tech Hub and what we do here, I can tell you about the facilities available," + "and I can tell you about events scheduled in the Tech Hub."
    return build_response({}, build_speechlet_response(card_title, speech_text, reprompt_text, False))


def facilities():
    """
    explains what the tech hub skill can do
    """
    card_title = "Welcome to the Tech hub"
    speech_text = "In the Tech Hub we have available 12 desks, 9 with 2 monitors and 3 with 1 monitor each. " + "We have a presentation area that seats 40 and a big telly. We also have a smart football table and our own wifi."
    return build_response({}, build_speechlet_response(card_title, speech_text, reprompt_text, False))


def add_value_to_db(name, quan_to_add, db):
    try:
        quantity = db.get_item(TableName='TechHubInventory', Key={'name': {'S': name}})
        quantity = int(quantity['Item']['quantity']['N'])
        db.update_item(TableName='TechHubInventory', Key={'name': {'S': name}},
                       UpdateExpression=' SET quantity = :newquantity ',
                       ExpressionAttributeValues={':newquantity': {'N': str(quantity + quan_to_add)}})
        return "There are now %s %s" % (quantity + quan_to_add, plu(name))
    except:
        db.update_item(TableName='TechHubInventory', Key={'name': {'S': name}},
                       UpdateExpression=' SET quantity = :newquantity ',
                       ExpressionAttributeValues={':newquantity': {'N': str(quan_to_add)}})
        return "There are now %s %s" % (quan_to_add, plu(name))


def rem_value_from_db(name, quan_to_rem, db):
    try:
        quantity = db.get_item(TableName='TechHubInventory', Key={'name': {'S': name}})
        quantity = int(quantity['Item']['quantity']['N'])
        if quantity >= quan_to_rem:
            db.update_item(TableName='TechHubInventory', Key={'name': {'S': name}},
                           UpdateExpression=' SET quantity = :newquantity ',
                           ExpressionAttributeValues={':newquantity': {'N': str(quantity - quan_to_rem)}})
            return "currently %s %s exists" % (quantity - quan_to_rem, plu(name))

        else:
            return "There are not enough %s to remove that many" % plu(name)
    except:
        "there were no %s found" % plu(name)


def list_items(db):
    output = 'here is what was found in the tech hub: '
    for i in db.scan(TableName='TechHubInventory')['Items']:
        output += ' ' + plu(str(i['name']['S']))
    return output


def get_item_quantities(name, db):
    output = db.get_item(TableName='TechHubInventory', Key={'name': {'S': name}})
    try:
        return "there are %s %s in the inventory" % (output['Item']['quantity']['N'], plu(name))
    except:
        return "there are no %s in the inventory" % plu(name)


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """
    print(
        "on_session_started requestId=" + session_started_request['requestId'] + ", sessionId=" + session['sessionId'])


def on_session_ended(event, session):
    print("on_session_ended requestId=" + session_ended_request['requestId'] + ", sessionId=" + session['sessionId'])
    return build_response('Good bye', True)


def on_intent(intent_request, session, db, dynamodb):
    print("on_intent requestId=" + intent_request['requestId'] + ", sessionId=" + session['sessionId'])
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    if intent_name == 'add_value_to_db':
        name = sing(intent_request['intent']['slots']['name']['value'])
        quan_to_add = int(intent_request['intent']['slots']['quan_to_add']['value'])
        outputSpeech = add_value_to_db(name, quan_to_add, dynamodb)
    elif intent_name == "TechHubExplainedIntent":
        return explanation()
    elif intent_name == "FunctionIntent":
        return functions()
    elif intent_name == "FacilitiesIntent":
        return facilities()
    elif intent_name == 'rem_value_from_db':
        name = sing(intent_request['intent']['slots']['name']['value'])
        quan_to_rem = int(intent_request['intent']['slots']['quan_to_rem']['value'])
        outputSpeech = rem_value_from_db(name, quan_to_rem, dynamodb)
    elif intent_name == 'list_items':
        outputSpeech = list_items(dynamodb)
    elif intent_name == 'get_item_quantities':
        name = sing(intent_request['intent']['slots']['name']['value'])
        outputSpeech = get_item_quantities(name, dynamodb)
    else:
        outputSpeech = "sorry but I didn't understand the request"
    return build_response(outputSpeech, False)


def on_session_ended(event, session):
    print("on_session_ended requestId=" + session_ended_request['requestId'] + ", sessionId=" + session['sessionId'])
    return build_response('Good bye', True)


# ------------ Main Handler ---------------
def lambda_handler(event, context):
    import boto3
    from pydblite import Base
    db = Base('/tmp/TechHub.pld')
    if db.exists():
        db.open()
    else:
        db.create('name', 'quantity')
        db.open()
    dynamodb = boto3.client('dynamodb')

    print("event.session.application.applicationId=" + event['session']['application']['applicationId'])

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        output = on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        output = on_intent(event['request'], event['session'], db, dynamodb)
    elif event['request']['type'] == "SessionEndedRequest":
        output = on_session_ended(event['request'], event['session'])
    db.commit()
    return output


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they want """
    print("on_launch requestId=" + launch_request['requestId'] + ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()
