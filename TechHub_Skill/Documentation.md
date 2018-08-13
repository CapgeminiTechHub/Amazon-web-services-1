# Introduction

The Tech Hub Alexa skill was initially built by Alex Pettifer, Jakir Ashraf and Luke Power, 
and then developed Jakir and Luke. 

This README outlines our development process, and attempts to justify the design of the skill. 

We began work for the skill on the 16th July 2018. For the first week we messed around with the technology, getting an idea of how skills are built. We developed some initial intents separately, and then combined them into a single python file. 

From here we used a personal git hub repository to make sure the most up to date, working version of the python and JSON code was available.

We initially developed intents separately because Luke was using java 8 and Jakir was using python. Python was decided upon as the common language because of its ease of learning. Additionally, there is a lot more support for python alexa skills as apposed to java 8.


# Meeting on 26/07/2018

This was our first major discussion about the use of the skill.

At this point we had a working prototype. We discussed 3 separate routes to go down to make user interaction easier:


1)	Use Tech Hub as the invocation name. This avoids using a secondary name for invocation such as assistant or helper. However, the downside is that not all intents flow well if the invocation name has to be used before the intent utterance. IE ‘ask the tech hub to tell me about the tech hub’.

Solution: upon further investigation, we found that the invocation name can be spoke after the intent utterance. IE ‘tell me about the Tech Hub’.We decided that this was the most intuitive of the three solutions and so continued down this route. However at first we only found limited success upon testing this solution. 

2)	Indirectly invoke the skill IE ‘tell me about facilities’ Then, as long as the skill includes a CanFulfillIntentRequest SPI, the Alexa works out which skill is being invoked. However, this was only available in US locals at the time of building. We didn't consider this route any furthur.  


3)	Use a secondary name like ‘helper’ or ‘assistant’ to invoke the skill. This allows the skill to be asked about the Tech Hub in context ie. ‘ask helper to tell me about the tech hub’. However, including a random name for invocation feels inefficient, and takes the focus off the Tech Hub. There is an argument that giving an Alexa skill a persona may add to the user experience, however this is traded for adding an unnecessary entity into every conversation about the Tech Hub.

We did intially go down this route, using 'phoenix' as the invocation name. And although this worked for development, in testing it was not recieved well. 

We concluded to follow the first solution, and decided to work through the design process found at https://developer.amazon.com/designing-for-voice/design-process/


# Meeting on 30/07/2018

We used an echo Dot device to test out intents. The majority of the utterances we tested were successful.
However, as we were using the alexa device, we felt that our intents did not 'flow' as naturally as human speech. We were having to say the invocation name 'tech hub' before saying each utterance. Otherwise the utterance was not always recognised.

Some intents would work using the intent name first ie. 'tell me about facilities in the tech hub'. Whilst others did not 'tell me about the tech hub'. This is because certain words are considered 'optional', and so cannot be used for intent utterances on their own. In the above example, 'about the' was the intended utterance. However, these words are considered optional by the alexa, since they exist only to make sentences easier for humans to say. Hence, they cannot be contained in utterances. Given this issue, we intially moved away from using 'tech hub' as the invocation name, only to return to it when it became clear it was the benefits outweighed the disadvantages.


By using 'Tech Hub' as the invocation name, questions such as 'tell me about the tech hub' meant that the only words to be used as an uttterance were 'about' and 'the'. This was not a strong enough utterance for Alexa to understand which intent was supposed to be invoked.

Testing with a different invocation name such as 'helper' gave us a higher sucess rate. As a result of this testing, we had a discussion and concluded to change the invocation to 'Phoenix'.

At this point our next step was to add more utterances and to keep the session open for certain intents to make interacting wiht the skill feel more conversational.

# The Following Week

We continued to refine the skill over the next couple of weeks. We considered using dialog.delegate to create multi dialog interactions. However, this functionality was taking up a lot of resources, and so in the end we decided to forgo it.

Instead we implemented some new intents to give the skill more functionality. We added intents to close inventory management sessions, to inform users of opening times, to explain how to book rooms in the tech hub, and who can use the tech hub.

We also changed the functions() intent, which explains what the skill does, to respond to the AMAZON.help intent, a built in intent. Following the design principles outlined for VUIs, we limited the help function to explaining 3 intents. This meant that we needed a 'moreOptions' intent, which listed the remaining functions of the skill. These functions left the session open so that the user could activate a follow up intent with out having to reinvoke the skill. 

We also implemented a proper fallback Intent. In the case of not understanding a response as an accepted utterance, the skill would reply with the functions() def, the same as the help intent. 

We also had to spent some time cleaning up utterances, some were too similair, which would result in the wrong intent being activated.

# Week Beginning 06/08/18

We had planned to demonstrate our skill on Monday, however we ran into a problem.. The invocation name was no longer opening our skill. We later learnt the reason for this was that we had multiple skills that were enabled and shared the same invocation name. This caused a clash and meant that an older verison of our skill was being invoked. We solved the issue by disabling testing for all other skills.

On Tuesday we gave a demonstration to Les Frost. From this test, we received the following feedback:

- Change the invocation name from 'Phoenix' back to 'Tech Hub'. The reason given was that users would be likely to call it tech hub and not phoenix, and that most of the intents would still work if tech hub was the invocation name.
  -- this did require changing the utterances for TechHubExplainedIntent however
- Research how cloud logs can be used to monitor the interactions with the alexa device. This should allow us to find errors with real usage and thus allow us to address the issues.
- Make the VUI more natural and easier for newcomers

In response to the latter point, we redesigned the help function to be more comprehensive. We created a branching path, where there is a sinlge help function, and 3 further options which explain all the different intents available. These 3 furthur options necessitated 3 more intents. 

This also meant changing some utterances to make sure that there were no clashes. After experimenting a bit we found that 'tech hub' could be used as both the invocation name and in the utterances, which helped the utterances sound more natural.

We also researched how to use cloud watch logs to make it easier to identify errors. To make the cloud watch logs more readable, we added print statements into every intent, so that we could distinguish which intent was activated. We also used the logger library to print a log statement each time an intent was activated. Combined with the information that the alexa web app tracks, we were confident that this would allow us to debug any errors.

# Wrapping Up

After a couple of days testing the new intents, we found that there was still one major error. The Skill would not always properly close. To remedy this, we implemented python code to explicitly handle the stop and close intents. This allowed us to extent the built-in utterances. The Skill now responded to 'Thank you' and 'goodbye' by closing the session and saying 'bye' to the user. This made the SKill feel more human-like.



