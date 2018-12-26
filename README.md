# Mighty Scraper

Template for a cost efficient website scraper that

- saves data to Google Sheets
- sends Slack notifications
- scheduled using AWS Lambda and CloudWatch

## Setting up
- Change config values in `google_sheets.py`
- Change config values in `slack.py`
- Read Medium article to configure Google API, Slack, AWS Lambda and CloudWatch

## Customization
- Scraping logic can be changed to scrape the website of your choice
- Google Sheets logic can be changed to add reading and updating data in addition to just adding new rows
- Slack notification logic can be changed to add conditions of when notifcations are fired
- and more!
