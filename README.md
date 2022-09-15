# Having Fun with Network Validation using Pyats and Phillips Hue APIs

![title-slide](_images/automates_1.jpg)

## Overview

This repository serves as an example, and overview of the workflow presented at Ansiblefest Chicago 2022, which leverages Ansible, Python and Pyats to leverage the Philips Hue Api for Network Validation.

> Note that the code in this repository can be used as a reference but will need modifications to work within your environment.

## Presentation

Traditionally network engineers have interfaced with devices using the command line interface. Gathering network state was a wieldy task involving trawling pages of configuration. Checking routes, neighbours and interface states was time consuming and error prone. Automation is changing the landscape of network management and configuration. We can easily create repeatable tasks that eliminate human error and reduce toil. Today Im going to show you how I gather structured data from Cisco devices using Pyats. I’ll then use the data I gather to perform network state validation and trigger API calls with Ansible.  
Hopefully this session will be a bit of fun and a little outside the box, the API’s I use will be directed at my Phillips Hue lights turning them on when a desired state is reached.  However, most of these techniques and code can be used when automating at scale in production environments, The code could easily be modified and built upon to trigger alarms and alerts in many customer networks using Ansible. For example instead of playing with visual cues we could easily trigger an alert in Slack or an email to the Ops team with some simple code amends.
