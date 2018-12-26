# -*- coding: utf-8 -*-
import arrow
import json
import requests


class Slack:

    # TODO
    WEBHOOK_URL = ''

    # TODO
    USERNAME = ''

    # TODO
    CHANNEL = ''

    def _post_slack_message(self, text):
        slack_data = {
            'text': text,
            'channel': self.CHANNEL,
            'username': self.USERNAME,
            'mrkdwn': True
        }

        requests.post(
            self.WEBHOOK_URL,
            data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}
        )

    def send_todays_notification(self, price):
        message = '*NEW PRICE*\n%s: $%s' % (
            str(arrow.utcnow().date()), price
        )
        self._post_slack_message(message)

    def test_notification(self):
        self.send_todays_notification(9999)


if __name__ == '__main__':
    Slack().test_notification()
