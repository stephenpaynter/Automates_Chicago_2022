# Having Fun with Network Validation using Pyats and Phillips Hue APIs

![title-slide](_images/automates_1.jpg)

## Overview

This repository serves as an example, and overview of the workflow presented at Ansiblefest Chicago 2022, which leverages Ansible, Python and Pyats to leverage the Philips Hue Api for Network Validation.

> Note that the code in this repository can be used as a reference but will need modifications to work within your environment.

## Presentation

Traditionally network engineers have interfaced with devices using the command line interface. Gathering network state was a wieldy task involving trawling pages of configuration. Checking routes, neighbours and interface states was time consuming and error prone. Automation is changing the landscape of network management and configuration. We can easily create repeatable tasks that eliminate human error and reduce toil. Today Im going to show you how I gather structured data from Cisco devices using Pyats. I’ll then use the data I gather to perform network state validation and trigger API calls with Ansible.  
Hopefully this session will be a bit of fun and a little outside the box, the API’s I use will be directed at my Phillips Hue lights turning them on when a desired state is reached.  However, most of these techniques and code can be used when automating at scale in production environments, The code could easily be modified and built upon to trigger alarms and alerts in many customer networks using Ansible. For example instead of playing with visual cues we could easily trigger an alert in Slack or an email to the Ops team with some simple code amends.


![title-slide](_images/automates_2.jpg)

Who am I? My name is Stephen Paynter. I’m based in the North East of England and have been a network engineer for over 25 years, predominantly working as an IT contractor in both private and public sectors.  I’m a Cisco CCIE and full time automation engineer.  I am presently automating at scale with AAP,  Ansible core and Python.   
I’m on most social media platforms so if you have any questions or feedback from todays session then hit me up and I’d be happy to help.  All the code from this session is also available In my Github.

![title-slide](_images/automates_3.jpg)

2020, what happened, a lot yeah. At least everyone knew where Wuhan was on a map by the end of March.

![title-slide](_images/automates_4.jpg)

For me personally what happened was I couldn’t do the hobbies I enjoyed. The UK like everywhere else mandated people stay at home. That meant no Surfing, wakeboarding,  Snowboarding or Mountain biking, Personally, that was giving up a lot. Being active and busy for me is like a fountain of youth, and im not really a happy bunny if I can’t do get my fix at least once or twice a week. A brief 30 minute walk during my lunch hour was the only thing keeping me marginally entertained.   

![title-slide](_images/automates_5.jpg)

This wasn’t sustainable, I needed something to fill my personal time and keep me sane during lockdown. Luckily Cisco had just released their Devnet certification track. This seemed a perfect solution, I was already automating in my current role and this would only make me a better engineer and expose me to new technologies and products. So after a month of indecision I decided to pursue it,  but I wanted to make the process as fun as possible. I find the older I get the more I struggle to learn. I needed a way to stay engaged and motivated whilst ensuring I understood what I needed to learn. 

![title-slide](_images/automates_6.jpg)

APIs are everywhere. There are so many public facing APIss available on the internet that anyone can interact with. 

![title-slide](_images/automates_7.jpg)

Believe it or not there’s a Star Wars API, here’s the return response from a query made to the spaceship resource. You can also query planets, vehicles, people, films and species . NASA has an API that amongst other things will tell you how many people are currently in space or how many near earth objects are currently being tracked. Theres also API’s for football, beer, countries, dinosaurs, marvel comics, if you can think it, there’s probably an API out there for it. 



