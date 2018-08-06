# Amazon Alexa - Tech Hub Skill

# Contents
#### 0. Overview
#### 1. Opening the skill
#### 2. Explain Tech Hub
#### 3. Functions
#### 4. Facilities
#### 5. Inventory


# Overview

The Tech Hub skill allows users to walk into the @Phoenix Tech Hub at Capgemini and ask questions about the tech hub. The skill respons to a variety of queries. 

Examples of the queries the Tech Hub skill can answer include the following:

- Tells me what the Tech Hub is
- Tells me what you can do
- Tells me about the facilities available in the Tech Hub
- Tell me what's in the inventory
- etc.

# Opening the skill

The invocation name for the Tech Hub skill is 'Phoenix'.
Saying phrases such as:

- "Open Phoenix"
- "Ask Phoenix"
- "[do something] from Phoenix"

will open the skill and perform an intent if applicable. Intents can be activated at the same time as, or after opening the skill.


# Explain Tech Hub

Asking questions such as:

- "Who are you?"
- "What goes on in this room?"
- "What is this place?"
- "Tell me about the tech hub."

as well as others, will cause Alexa to respond by explaining the purpose of the Tech Hub.


# Help

If the skill is invoked but no intent is uttered, the launch request prompts the user to ask for help.

- "help"
- "help me"

Will prompt Alexa to respond with a list of the functions Phoenix can do. It also offers more options for the user to explore.


# More Options

This intent acts as part two of the help function. it is activated by utterances such as:

- "more options"
- "other options"

Like the help intent, it leaves the session open so that the user can activate another intent rather than having to reinvoke the skill.


# Facilities

Asking questions such as:

- "What equipment do you have"
- "What facilities are available?"
- "What kit is available?"

These questions and similar questions will prompt Alexa to tell the user about the facilities available i.e number of computers in the area, the number of desks etc.


# Inventory

The inventory keeps track of the quantity of various items in the Tech Hub. Users can add/remove and find out the number of an item currently in the Tech Hub.

Supported items include:    "desks", "mice", "keyboards", "monitors", "chargers", "raspberry pies", "brick pies", "screens", "mind storms set", "raspberry pie camera", "brick pie", "keyboard", "mouse", "desk", "laptop", "charger", "raspberry pie", "screen"

## Viewing Inventory

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

## Closing the Inventory

This intent is activated with utterances suchs as:

- "close the inventory"
- "i'm finished with the inventory"
- "lock the inventory"
- "shut the inventory"

This intent fullfills the purpose of closing the session for inventory management.

