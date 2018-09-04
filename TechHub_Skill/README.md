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

This intent is the first branch of the root help function. it is activated by utterances such as:

- "more options"
- "other options"
- "more info"

The main difference between these branching functions and the main help function, is that these sessions do not leave the session open. If the user wants to ask Alexa about one of the other intents, they must reinvoke the skill.

## More details

Asking questions such as:

- "give me more details"
- "tell me more details about the tech hub"

will prompt Alexa to respond with a detailed explanation of the Tech Hub.

## Opening & Closing times

Asking questions such as:

- "what are the opening times?"
- "What are the closing time?"

as well as others, will prompt Alexa to respond with the opening and closing times.

## Facilities

Asking questions such as:

- "What equipment do you have?"
- "What facilities are available?"
- "What kit is available?"

will prompt Alexa to tell the user about the available facilites in the Tech Hub (this is different to the inventory).

# 4. Events

This intent is the second branch. it is activated by utterances such as:

- "what events are on?"
- "How do I book events?"

which will prompt Alexa to respond with the corresponding details. Rather than listing more intents to be activated afterwards, this intent delivers the relevant information right away. 

# 5. Inventory Management

The 3rd branch from the root help function. The inventory keeps track of the quantity of various items in the Tech Hub. Users can add/remove items, as well as querying how many of one item is in the database. Alternatively, they can ask for a list of all the items in the database.

Supported items include:   "pens",  "post-it notes", "chromecasts", "taggers", "echo dots", "laptops", "mice", "keyboards", "monitors", "chargers", "raspberry pies",  "t-shirts"

If the user attempts to add an unsupported item to the inventory, they will recieve an error message.


## Quantity

This intent can be activated by saying the following phrases:

- "How many [item] do we have?"
- "How many [item] are in the inventory?"

This returns the amount of one specific item in the inventory, the quantity may be zero but not negative.


## Adding Item to Inventory

This intent can be activated by saying the following phrases:

- "Add [quantity] [item]"
- "Add [quantity] [item] to the tech hub" 
- "Add [quantity] [item] to the Inventory"

Both slots must be filled for this intent to activate correctly. The Alexa confirms the quantity and name of the item, as well as the new total.

## Removing Item from Inventory

This intent can be activated by saying the following phrases:

- "Remove [quantity] [item]"
- "Remove [quantity] [item] from the tech hub" 
- "Remove [quantity] [item] from the Inventory"

As above, both slots must be filled for this intent to activate correctly. The Alexa confirms the quantity and name of the item, as well
as the new total.

## Listing All Items in Inventory

- "What is in the inventory"
- "What do we have"

This intent does not list the number of items, just all the different types of items.


## Close Inventory

This intent is activated with utterances suchs as:

- "close the inventory"
- "i'm finished with the inventory"
- "lock the inventory"
- "shut the inventory"

This intent fullfills the purpose of closing the session for inventory management. However it works at any time, whether in inventory management or not.

# 6. Closing the skill

Saying the following phrases will cause the skill to close midsession, its most useful after accidentally activating an intent.

- "cancel"
- "goodbye"
- "thank you"

