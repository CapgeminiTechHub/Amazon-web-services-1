# Amazon Alexa - Tech Hub Skill

# Contents

####  0. Overview

####  1. Opening the skill

####  2. Help

####  3. More Info
    - Explain Tech Hub
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

The Tech Hub skill allows users to walk into the @Phoenix Tech Hub at Capgemini and ask questions about the tech hub. The skill responds to a variety of queries. 

Examples of the queries the Tech Hub skill can answer include the following:

- Tells me what the Tech Hub is
- Tells me what you can do
- Tells me about the facilities available in the Tech Hub
- Tell me what's in the inventory
- etc.

As soon as the skill is open, you have 2 options:
1. Use help function to find out the possible phrases you can ask or..
2. Directly say your phrase (good if you already know the functionalities available)

![Diagram](https://github.com/OnwardPyrite/Amazon-web-services/blob/master/TechHub_Skill/diagram-alexa.PNG)

# 1. Opening the skill

The invocation name for the Tech Hub skill is 'Tech Hub'.
Saying phrases such as:

- "Open Tech Hub"
- "Ask Tech Hub ..."
- "[do something] from Tech Hub"

will open the skill and perform an intent if applicable. Intents can be activated at the same time as, or after opening the skill.

# 2. Help

Saying phrases such as:

- "Help"
- "Help me"

will prompt Alexa to tell the user the range of functionalities available within the skill.

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

