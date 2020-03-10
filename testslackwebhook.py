from datetime import date, datetime, timedelta
import requests
import json
from auth_slack import slack_webhook_url

today = datetime.now().strftime('%Y-%m-%d')

# Here is where we can format the slack message, it will output any holiday with todays
message = str(today) + ' important message!'
print('Sending simple message to security channel...')
slackmsg = {'text': message}
# Using the module json it formats it where the slack API can accept it
response = requests.post(slack_webhook_url, data=json.dumps(slackmsg), headers={'Content-Type': 'application/json'})
if response.status_code != 200:
    raise ValueError('Request to slack returned an error %s, the response is:\n%s' % (response.status_code, response.text))
print('Request completed!')

print('Sending image message to security channel...')
slackmsg2 = {
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Same changes recently:"
			}
		},
		{
			"type": "image",
			"title": {
				"type": "plain_text",
				"text": "image1",
			},
			"image_url": "https://i.imgur.com/AANszpb.jpg",
			"alt_text": "image1"
		}
	]
}

# Using the module json it formats it where the slack API can accept it
response = requests.post(slack_webhook_url, data=json.dumps(slackmsg2), headers={'Content-Type': 'application/json'})
if response.status_code != 200:
    raise ValueError('Request to slack returned an error %s, the response is:\n%s' % (response.status_code, response.text))
print('Request2 completed!')

