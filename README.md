# Mighty Scraper

Template for a cost efficient website scraper that

- saves data to Google Sheets
- sends Slack notifications
- scheduled using AWS Lambda and CloudWatch

Full instructions here:

https://medium.com/@yoheio/periodically-scraping-websites-saving-to-google-sheets-and-firing-slack-notifications-94a6b837d9a4

## Setting up
- set up virtualenv
- `pip install -r requirements.txt`
- Change config values in `google_sheets.py`
- Change config values in `slack.py`
- Read [Medium article](https://medium.com/@yoheio/periodically-scraping-websites-saving-to-google-sheets-and-firing-slack-notifications-94a6b837d9a4) to configure Google API, Slack, AWS Lambda and CloudWatch

## Python version
Tested using python 3.6.0

## Customization
- Scraping logic can be changed to scrape the website of your choice
- Google Sheets logic can be changed to add reading and updating data in addition to just appending new rows
- Slack notification logic can be changed to add conditions of when notifcations are fired
- and more!
