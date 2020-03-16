# upload 1 image every 5 minutes
from picamera import PiCamera
from datetime import datetime
import os
import time
import dropbox
from auth_dbox import (dropbox_access_token)
import logging
from imgurpython import ImgurClient
from auth_imgur import imgur_client_id,imgur_client_secret
from imageutil import ImageUtil
from notification import SlackNotificator


base_path = os.path.dirname(os.path.realpath(__file__))
# DBFILENAME = "./db.json"
# active days
MON = 0
TUE = 1
WED = 2
THU = 3
FRI = 4
SAT = 5
SUN = 6
# active hour ranges
HHMM1MIN = 800
HHMM1MAX = 1300
HHMM2MIN = 1800
HHMM2MAX = 2100
logging.basicConfig(filename='log_files/app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',level=logging.INFO)


def capture(filename):
    photo_path = '%s/static/photos/%s' % (base_path, filename)
    with PiCamera() as camera:
        camera.resolution = (640, 400)
        camera.capture(photo_path)
    return photo_path


def dbx_upload(filename, photo_path):
    dropbox_path = '/%s' % (filename)
    client = dropbox.Dropbox(dropbox_access_token)
    logging.info('Dropbox account linked')

    client.files_upload(open(photo_path, "rb").read(), dropbox_path)
    logging.info('File uploaded '.format(photo_path))

    return 1


def imgur_upload(photo_path):
    client = ImgurClient(imgur_client_id, imgur_client_secret)

    result = client.upload_from_path(photo_path, config=None, anon=True)
    logging.info('File uploaded to imgur '.format(result['link']))

    return result['link']


def compare_last_images():
    # get last image
    imagelast = '%s/static/photos/%s' % (base_path, 'imgX.jpg')
    # capture now image
    imagenow = '%s/static/photos/%s' % (base_path, 'imgY.jpg')
    with PiCamera() as camera:
        camera.resolution = (640, 400)
        camera.capture(imagenow)
    # compare
    if os.path.isfile(imagelast):
        logging.info("File imagelast exist")
        iutil = ImageUtil(imagelast, imagenow)
        ssim = iutil.compare_images
        logging.info("Structural Similarity: ",ssim)
        if ssim<0.90:
            # upload to imgur
            i1link = imgur_upload(imagelast)
            i2link = imgur_upload(imagenow)
            # notify with webhook
            logging.info('Notification - 2 images are differents')
            SlackNotificator.sendmsgimg2("Se detectó movimiento",i1link,i2link)
        # delete imagelast
        os.remove(imagelast)
    else:
        logging.info("Image last not not exist")
    # save imagenow as imagelast
    os.rename(imagenow,imagelast)
    logging.info("images renamed ok")

    return 1


def save_image(dt):
    wd = dt.weekday()
    hhmm = dt.hour*100+dt.minute
    if wd in (MON,TUE,WED,THU,FRI):
        if HHMM1MIN <= hhmm <= HHMM1MAX:
            return True
        elif HHMM2MIN <= hhmm <= HHMM2MAX:
            return True

    return False


if __name__ == '__main__':
    logging.info('Start application')
    done = False
    while True:
        # check if task is done
        if done:
            logging.info('ALL DONE')
            break
        else:
            datenow = datetime.now()
            # upload to dropbox every 5 minutes
            if datenow.minute%5==0 and save_image(datenow):
                timestamp = datenow.isoformat()
                filename = 'img%s.jpg' % timestamp
                photo_path = capture(filename)
                dbx_upload(filename, photo_path)
            # check for diferences every 1 minute
            compare_last_images()
            # sleep 1 minutes
            time.sleep(60)
            continue

