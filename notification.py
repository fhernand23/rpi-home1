from twitter import *
# twitter client: https://github.com/sixohsix/twitter
from auth_tw import (consumer_key,consumer_secret,access_token,access_token_secret)
from auth_slack import slack_webhook_url
import requests
import json


class TwNotificator():
    def __init__(self):
        self.t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

    def senddm(self, dest, msg):
        self.t.direct_messages.events.new(
            _json={
                "event": {
                    "type": "message_create",
                    "message_create": {
                        "target": {
                            "recipient_id": self.t.users.show(screen_name=dest)["id"]},
                        "message_data": {
                            "text": msg}}}})

    def senddmimg(self, dest, msg, imgpath):
        # Send images along with your tweets:
        # - first just read images from the web or from files the regular way:
        with open(imgpath, "rb") as imagefile:
            imagedata = imagefile.read()
        # - then upload medias one by one on Twitter's dedicated server
        #   and collect each one's id:
        t_upload = Twitter(domain='upload.twitter.com',
                           auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))
        id_img1 = t_upload.media.upload(media=imagedata)["media_id_string"]
        print("media id " + str(id_img1))

        self.t.direct_messages.events.new(
            _json={
                "event": {
                    "type": "message_create",
                    "message_create": {
                        "target": {
                            "recipient_id": self.t.users.show(screen_name=dest)["id"]},
                        "message_data": {
                            "text": msg,
                            "attachment": {
                                "type": "media",
                                "media": {
                                    "id": id_img1}}}}}})


class SlackNotificator():
    def sendmsg(self,msg):
        slackmsg = {'text': msg}
        # Using the module json it formats it where the slack API can accept it
        response = requests.post(slack_webhook_url, data=json.dumps(slackmsg),
                                 headers={'Content-Type': 'application/json'})
        if response.status_code != 200:
            raise ValueError(
                'Request to slack returned an error %s, the response is:\n%s' % (response.status_code, response.text))


    def sendmsgimg(self,msg,imgurl):
        slackmsg = {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": msg
                    }
                },
                {
                    "type": "image",
                    "title": {
                        "type": "plain_text",
                        "text": "image1",
                    },
                    "image_url": imgurl,
                    "alt_text": "image1"
                }
            ]
        }
        response = requests.post(slack_webhook_url, data=json.dumps(slackmsg),
                                 headers={'Content-Type': 'application/json'})
        if response.status_code != 200:
            raise ValueError(
                'Request to slack returned an error %s, the response is:\n%s' % (response.status_code, response.text))


    def sendmsgimg2(self,msg,imgurl,imgurl2):
        slackmsg = {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": msg
                    }
                },
                {
                    "type": "image",
                    "title": {
                        "type": "plain_text",
                        "text": "image1",
                    },
                    "image_url": imgurl,
                    "alt_text": "image1"
                },
                {
                    "type": "image",
                    "title": {
                        "type": "plain_text",
                        "text": "image2",
                    },
                    "image_url": imgurl2,
                    "alt_text": "image2"
                }
            ]
        }
        response = requests.post(slack_webhook_url, data=json.dumps(slackmsg),
                                 headers={'Content-Type': 'application/json'})
        if response.status_code != 200:
            raise ValueError(
                'Request to slack returned an error %s, the response is:\n%s' % (response.status_code, response.text))

