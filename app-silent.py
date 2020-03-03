# upload 1 image every 5 minutes
from flask import Flask, render_template
from picamera import PiCamera
from datetime import datetime
import os
import time
import dropbox
from auth_dbox import (dropbox_access_token)


app = Flask(__name__)

path = os.path.dirname(os.path.realpath(__file__))
DBFILENAME = "./db.json"


def capture(filename):
    photo_path = '%s/static/photos/%s' % (path, filename)
    with PiCamera() as camera:
        camera.resolution = (640, 400)
        camera.capture(photo_path)
    return photo_path


def upload(filename,photo_path):
    dropbox_path = '/rpihomehz/%s' % (filename)
    client = dropbox.Dropbox(dropbox_access_token)
    print("[SUCCESS] dropbox account linked")

    client.files_upload(open(photo_path, "rb").read(), dropbox_path)
    print("[UPLOADED] {}".format(photo_path))

    return 1

if __name__ == '__main__':
    print("Start application")
    done = False
    while True:
        # check if task is done
        if done:
            print('ALL DONE')
            break
        else:
            timestamp = datetime.now().isoformat()
            filename = 'img%s.jpg' % (timestamp)
            photo_path = capture(filename)
            upload(filename,photo_path)
            # sleep 5 minutes
            time.sleep(300)
            continue

