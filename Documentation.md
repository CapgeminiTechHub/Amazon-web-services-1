# Introduction

The Tech Hub Alexa skill was initially built by Alex Pettifer, Jakir Ashraf and Luke Power 
and then developed more by Jakir and Luke. 

This read me outlines our development process, and attempts to justify the design of the skill. 

We began work for the skill on the 16th July 2018. 
For the first week we messed around with the technology, getting an idea of how skills are built.
We developed some initial intents separately, and then combined them into a single python file. 

From here we used a personal git hub repository to make sure the most up to date, working version of the code was available.

We initially developed intents separately because Luke was using java 8 and Jakir was using python. 
Python was decided upon as a common language because of its easy of learning. Also there was a lot more support for python alexa skills.


# Meeting on 26/07/2018

This was our first major discussion about the use of the skill.

At this point we had  a working prototype. We discussed 3 separate routes to go down to make user interaction easier


1)	Use Tech Hub as the invocation name. This has the advantage that it doesn’t require using a secondary name for invocation such as assistant or helper. But there is the downside that it doesn’t flow well syntactically if the invocation name has to be used before the intent utterance. IE ‘ask the tech hub to tell me about the tech hub’
Solution: upon further investigation, invocation name can be spoke after intent utterance. IE ‘tell me about the Tech Hub’
We decided that this was the most intuitive of the three solutions and so continued down this route.


2)	Indirectly invoke the skill IE ‘tell me about facilities’ Then, as long as the skill includes a CanFulfillIntentRequest SPI, the Alexa works out which skill is being invoked. However, this was only available in US locals at the time of building.  


3)	Use a secondary name like ‘helper’ or ‘assistant’ to invoke the skill. This allows the skill to be asked about the Tech Hub in context IE ‘ask helper about to tell me about the Tech Hub’. However, including a random name for invocation feels inefficient, and takes the focus off the Tech Hub. There is an argument that giving an Alexa skill a persona may add to the user experience, however this is traded for adding an unnecessary entity into every conversation about the Tech Hub.

We concluded to follow the first solution, and decided to work through the design process found at https://developer.amazon.com/designing-for-voice/design-process/


# Meeting on 30/07/2018

In this meeting, we decided to change the invocation to 'Phoenix'

After realising using Tech Hub as an invocation name led to problems, such as clashing intents with the invocation name, we changed the invocation name to 'Phoenix'.

