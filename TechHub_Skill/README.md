# Amazon Alexa - Tech Hub Skill

# Contents

####  0. Overview

####  1. Opening the skill

####  2. Help

####  3. More Info
    - Tech Hub Details
    - Opening & Closing times
    - Facilities
####  4. Events & Bookings
####  5. Inventory Management
    - Quantity
    - Add item(s)
    - Remove item(s)
    - List items
    - Close Inventory

####  6. Closing the skill

# 0. Overview

The Tech Hub skill allows users to walk into the Capgemini Tech Hub @Phoenix and ask an alexa device about the Tech Hub. 

Examples of the questions the Tech Hub skill can answer include the following:

- Tell me what the opening times for the tech hub are
- Tell me about the facilities available in the Tech Hub
- Tell me what's in the inventory
- etc.

# 1. Opening the skill

The skill must first be invoked, using the invocation name 'Tech Hub'.
Saying phrases such as:

- "Open Tech Hub"
- "Ask Tech Hub ..."
- "[do something] from Tech Hub"

will open the skill and perform an intent if applicable. Intents can be activated at the same time as, or after opening the skill.

After the skill has been invoked, the skill says a welcome greeting. At this point the conversation will follow one of two routes:
1. The user will activate the help function as prompted. This will allow an unexperiecned user to learn about the functions the skill provides
2. The User will directly speak an utterance becuase they know which intent they want to activate



# 2. Help

The help intent is the first part of a 2 stage process to inform a user about the actions the skill can perform for them.  

Saying phrases such as:

- "Help"
- "Help me"

will prompt Alexa to highlight 3 furthur intents which can be activated right after. These intents are: More Info; Events; and Inventory Management. These 3 options branch out to cover all the intents of the skill.

Represented visually:

![Diagram](https://github.com/OnwardPyrite/Amazon-web-services/blob/master/TechHub_Skill/diagram-alexa.PNG)

# 3. More Info

This intent acts as part one of the help function. it is activated by utterances such as:

- "more options"
- "other options"
- "more info"

Like the help intent, it leaves the session open so that the user can activate another intent rather than having to reinvoke the skill.

## Explain Tech Hub

Asking questions such as:

- "Who are you?"
- "What goes on in this room?"
- "What is this place?"
- "Tell me about the tech hub."

as well as others, will cause Alexa to respond by explaining the purpose of the Tech Hub.

## Opening & Closing times

Asking questions such as:

- "what are the opening times"
- "What are the closing times"

as well as others, will cause Alexa to respond with the opening/closing times.

## Facilities

Asking questions such as:

- "What equipment do you have"
- "What facilities are available?"
- "What kit is available?"

These questions and similar questions will prompt Alexa to tell the user about the facilities available i.e number of computers in the area, the number of desks etc.

# 4. Events

This intent acts as part two of the help function. it is activated by utterances such as:

- "what events are on?"
- "How do I book events"

will allow Alexa to respond with the corresponding details.

# 5. Inventory Management

The inventory keeps track of the quantity of various items in the Tech Hub. Users can add/remove and find out the number of an item currently in the Tech Hub. This intent acts as part three of the help function.

Supported items include:    "desks", "mice", "keyboards", "monitors", "chargers", "raspberry pies", "brick pies", "screens", "mind storms set", "raspberry pie camera", "brick pie", "keyboard", "mouse", "desk", "laptop", "charger", "raspberry pie", "screen"


## Quantity

This intent can be activated by saying the following phrases:

- "How many [item] do we have?"
- "How many [item] are in the inventory?"


## Adding Item to Inventory

This intent can be activated by saying the following phrases:

- "Add [quantity] [item]"
- "Add [quantity] [item] to the tech hub" 
- "Add [quantity] [item] to the Inventory"


## Removing Item from Inventory

This intent can be activated by saying the following phrases:

- "Remove [quantity] [item]"
- "Remove [quantity] [item] from the tech hub" 
- "Remove [quantity] [item] from the Inventory"


## Listing All Items in Inventory

- "What is in the inventory"
- "What do we have"

This intent does not list the number of items, just the different types of items.


## Close Inventory

This intent is activated with utterances suchs as:

- "close the inventory"
- "i'm finished with the inventory"
- "lock the inventory"
- "shut the inventory"

This intent fullfills the purpose of closing the session for inventory management.

# 6. Closing the skill

Saying the following phrases will cause the skill to close:

- "cancel"
- "goodbye"
- "thank you"

