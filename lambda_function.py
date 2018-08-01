# @authors Luke Power, Jakir Ashraf, Alex Pettifer for Capgemini
# @version 25/07/18

from __future__ import print_function
import boto3

CardTitlePrefix = "Tech Hub"

# --------------- Helpers that build all of the responses ----------------------
# Build a speechlet JSON representation of the title, output text,
# reprompt text & end of session
def build_speechlet_response(title, output, reprompt_text, should_end_session):

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


# Build the full response JSON from the speechlet response
def build_response(session_attributes, speechlet_response):

    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------
#                TODO
# 1) fix plural and singular nouns
#
# ===========================
# Converts plural to singular
# ===========================
def sing(string):

    import inflect
    p = inflect.engine()
    words = string.split(' ')
    last_word = words.pop(len(words) - 1)
    output = p.singular_noun(last_word)
    if output:
        return ' '.join(words + [output])
    else:
        return ' '.join(words + [last_word])


# ===========================
# Converts singular to plural
# if the count is greater than
# one.
# ===========================
def plu(string, count=2):

    import inflect
    p = inflect.engine()
    return p.plural(string, count)


# --------------- Functions that control the skill's behavior ------------------
# invoked on launch
def get_welcome_response():
    session_attributes = {}
    card_title = "Hello and welcome"
    speech_output = "Hello. Welcome to the Tech Hub. Say Help if you want to know what I can do"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I'm sorry - I didn't understand. How can I help you?"
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


# invoked on close
def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Have a nice day! "
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


# explains what the tech hub is
def explanation():

    card_title = "Welcome to the Tech hub"
    speech_text = "The Tech Hub is a place of innovation. " + "We believe that technology is worth sharing, which is why we explore new ways to use emerging tech. " + "Current projects include developing skills for Alexa and Amazon Deep-lens, as well as using " + "rasberry pies in creative experiments. Tweet-us at hash tag Tech-Hub."
    reprompt_text = "I'm sorry - I didn't understand. Try asking me to explain myself"
    return build_response({}, build_speechlet_response(card_title, speech_text, reprompt_text, True))


# explains what the tech hub skill can do
def functions():

    card_title = "Welcome to the Tech hub"
    speech_text = "Hello. I can tell you about the Tech Hub and what we do here. I can tell you about the facilities available." + " And I can tell you about events scheduled in the Tech Hub. Say other options to hear more."
    reprompt_text = "I'm sorry - I didn't understand. Try asking me what I can do"
    return build_response({}, build_speechlet_response(card_title, speech_text, reprompt_text, False))

# explains what the tech hub skill can do
def whoCanUseThisPlace():

    card_title = "Welcome to the Tech hub"
    speech_text = "The tech hub is open to everyone. View the tech hub calendar on Outlook to see if events are happening here."
    reprompt_text = "I'm sorry - I didn't understand. Please try again "
    return build_response({}, build_speechlet_response(card_title, speech_text, reprompt_text, True))

# room bookings
def howDoIBookThisRoom():

    card_title = "Welcome to the Tech hub"
    speech_text = "You can book this room and others using the outlook calendar"
    reprompt_text = "I'm sorry - I didn't understand. Please try again "
    return build_response({}, build_speechlet_response(card_title, speech_text, reprompt_text, True))

# opening/closing times
def openCloseTimes():

    card_title = "Welcome to the Tech hub"
    speech_text = "The tech hub is open from nine till five"
    reprompt_text = "I'm sorry - I didn't understand. Please try again "
    return build_response({}, build_speechlet_response(card_title, speech_text, reprompt_text, True))


# explains what the tech hub skill can do
def events():

    card_title = "events in the tech hub"
    speech_text = "To manage events for the Tech hub, then ask me what's on the calendar."
    reprompt_text = "I'm sorry - I didn't understand. Try asking me what I can do"
    return build_response({}, build_speechlet_response(card_title, speech_text, reprompt_text, False))


# explains what the tech hub skill can do
def facilities():

    card_title = "Welcome to the Tech hub"
    speech_text = "In the Tech Hub we have available 12 desks, 9 with 2 monitors and 3 with 1 monitor each. " + "We have a presentation area that seats 40 and a big telly. We also have a smart football table and our own wifi."
    reprompt_text = "I'm sorry - I didn't understand. Try asking me what facilities are available"
    return build_response({}, build_speechlet_response(card_title, speech_text, reprompt_text, True))


# adds items to inventory
def add_value_to_db(name, quan_to_add, db):
    card_title = "Tech Hub"
    reprompt_text = "I'm sorry - I didn't understand. How can I help you?"
    try:
        quantity = db.get_item(TableName='TechHubInventory', Key={'name': {'S': name}})
        quantity = int(quantity['Item']['quantity']['N'])
        db.update_item(TableName='TechHubInventory', Key={'name': {'S': name}},
                       UpdateExpression=' SET quantity = :newquantity ',
                       ExpressionAttributeValues={':newquantity': {'N': str(quantity + quan_to_add)}})
        if quantity + quan_to_add > 1:
            output = "I have added %s %s to the inventory. " %(quan_to_add, plu(name)) + " There are now %s %s in the inventory" % (quantity + quan_to_add, plu(name))
        else:
            output = "I have added %s %s to the inventory. " %(quan_to_add, sing(name)) + " There is now %s %s in the inventory" % (quantity + quan_to_add, sing(name))
    except:
        db.update_item(TableName='TechHubInventory', Key={'name': {'S': name}},
                       UpdateExpression=' SET quantity = :newquantity ',
                       ExpressionAttributeValues={':newquantity': {'N': str(quan_to_add)}})
        if quan_to_add + quantity > 1:
            output = "There are now %s %s in the inventory" % (quan_to_add, plu(name))
        else:
            output = "There is now %s %s in the inventory" % (quan_to_add, plu(name))

    return build_response({}, build_speechlet_response(card_title, output, reprompt_text, False))


#removes item from inventory
def rem_value_from_db(name, quan_to_rem, db):
    card_title = "Tech Hub"
    reprompt_text = "I'm sorry - I didn't understand. How can I help you?"
    try:
        quantity = db.get_item(TableName='TechHubInventory', Key={'name': {'S': name}})
        quantity = int(quantity['Item']['quantity']['N'])
        if quantity >= quan_to_rem:
            db.update_item(TableName='TechHubInventory', Key={'name': {'S': name}},
                           UpdateExpression=' SET quantity = :newquantity ',
                           ExpressionAttributeValues={':newquantity': {'N': str(quantity - quan_to_rem)}})
            if quantity - quan_to_rem > 1:
                output = "I have removed %s %s from the inventory. " %(quan_to_rem, plu(name)) + " currently there are now %s %s" % (quantity - quan_to_rem, plu(name))
            elif quantity - quan_to_rem == 1:
                output = "I have removed %s %s from the inventory. " %(quan_to_rem, sing(name)) + " currently there is %s %s" % (quantity - quan_to_rem, sing(name))
            else:
                output = "currently there are %s %s" % (quantity - quan_to_rem, plu(name))
        else:
            output = "There are not enough %s to remove that many" % plu(name)
    except Exception as e:
        # output = "there were no %s found" % plu(name)
        output = e

    return build_response({}, build_speechlet_response(card_title, output, reprompt_text, False))


# returns a list of all items in the inventory
def list_items(db):
    card_title = "List of items in inventory"
    reprompt_text = "I'm sorry - I didn't understand. How can I help you?"
    output = 'here is what was found in the tech hub: '
    for i in db.scan(TableName='TechHubInventory')['Items']:
        output += ' ' + plu(str(i['name']['S'])) + ','
    return build_response({}, build_speechlet_response(card_title, output, reprompt_text, False))


# returns the amount of an item
def get_item_quantities(name, db):
    card_title = "List of items in inventory"
    reprompt_text = "I'm sorry - I didn't understand. How can I help you?"
    output_text = ""

    try:
        output = db.get_item(TableName='TechHubInventory', Key={'name': {'S': name}})
    except:
        output = "there are no %s in the inventory" % plu(name)

    output_text = "there are %s %s in the inventory" % (output['Item']['quantity']['N'], plu(name))

    return build_response({}, build_speechlet_response(card_title, output_text, reprompt_text, False))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """
    print(
        "on_session_started requestId=" + session_started_request['requestId'] + ", sessionId=" + session['sessionId'])


def on_session_ended(session_ended_request, session):
    print("on_session_ended requestId=" + session_ended_request['requestId'] + ", sessionId=" + session['sessionId'])
    return build_response('Good bye', True)


# identifies which intent is invoked
def on_intent(intent_request, session, db, dynamodb):
    print("on_intent requestId=" + intent_request['requestId'] + ", sessionId=" + session['sessionId'])
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    if intent_name == 'add_value_to_db':
        name = sing(intent_request['intent']['slots']['name']['value'])
        quan_to_add = int(intent_request['intent']['slots']['quan_to_add']['value'])
        return add_value_to_db(name, quan_to_add, dynamodb)
    elif intent_name == "TechHubExplainedIntent":
        return explanation()
    elif intent_name == "AMAZON.HelpIntent" | intent_name == "AMAZON.FallbackIntent":
        return functions()
    elif intent_name == "FacilitiesIntent":
        return facilities()
    elif intent_name == "EventsIntent":
        return events()
    elif intent_name == "WhenDoesThisPlaceOpenClose":
        return openCloseTimes()
    elif intent_name == "HowDoIBookThisRoom":
        return howDoIBookThisRoom()
    elif intent_name == "CanAnyoneUseThisPlace":
        return whoCanUseThisPlace()
    elif intent_name == 'rem_value_from_db':
        name = sing(intent_request['intent']['slots']['name']['value'])
        quan_to_rem = int(intent_request['intent']['slots']['quan_to_rem']['value'])
        return rem_value_from_db(name, quan_to_rem, dynamodb)
    elif intent_name == 'list_items':
        return list_items(dynamodb)
    elif intent_name == 'get_item_quantities':
        name = sing(intent_request['intent']['slots']['name']['value'])
        return get_item_quantities(name, dynamodb)
    else:
        outputSpeech = "sorry but I didn't understand the request"
        return build_response(outputSpeech, False)


# ------------ Main Handler ---------------
def lambda_handler(event, session):
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


# invoked by launch request
def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they want """
    print("on_launch requestId=" + launch_request['requestId'] + ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()
