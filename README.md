# gamechanger-automation
Scripts to support automation of Game Changer schedules

## Description

Gamechanger is a popular app for managing sports teams including scheduling, scoring, communication, and stats gathering. However, it doesn't support an API or upload process for multiple events. This project uses Selenium to log into the account and use a CSV as input to generate events.

## Project Setup

This project uses Poetry for managing dependencies. I've tried to keep it small with only leveraging Selenium. You may need to install drivers depending on your setup (read more [here](https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test)).

As of v0.1, I simply ran manually through my IDE.

## Spreadsheet Setup

I've included a spreadsheet(data-formatter.xlsx) which will help set up the right values to be used. The "transformed" tab has the format with all the right details necessary. Simply copy and paste that to a csv (a la inputs.csv) to be read in. This does have data validation on the required fields to ensure consistency.

## Current state

As of v0.1 this is very rough and needs to be run manually. I was able to get this to work by iterating manually and adjusting things on the page as they were wrong. Many of the fields are type-aheads or require certain lookups which makes it slightly difficult to automate. At least it entered about 80% of the data correctly!

## Work Items

|Item|Description|State|
|----|----|---|
|Login Code|Currently, it sends a code to your email. I have it setup to take that as an input, but it's not correctly clicking the login button|:construction:|
|Error Handling|There is none!|:construction:|
|Logging|There is none!|:construction:|
|Team lookup|Currently team ids need to be specified in `.env`, see if there is a way to look it up in the Teams screen|:construction:|
|Better iteration|Iterate through the list rather than with `range`|:construction:|
|Event Validation|Handle different event types and validate inputs|:construction:|
|Class structures?|Explore mapping this to classes for improved validation|:construction:|
|Time Field|Currently has to be set character by character... see if that can be fixed|:construction:|
|Duration Field|In debgging, sets the right field but not when run as part of a batch|:construction:|
|Location|Need to handle the type-ahead search|:construction:|
|Opponent|This is messy...unsure how exactly to handle|:construction:|
|Review step|If we can get most of the data populated, perhaps keep the review step before creating the next one|:construction:|
|Code reorg|It's a mess!|:construction:|
|Type hints|Add them!|:construction:|