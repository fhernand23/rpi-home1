from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
import time
from notification import TwNotificator
import os


basepath = os.path.dirname(os.path.realpath(__file__))
pir = MotionSensor(4)
camera = PiCamera()
notificator = TwNotificator()

while True:
    pir.wait_for_motion()
    print("Motion detected!")
    # take picture
    timestamp = datetime.now().isoformat()
    photo_path = '%s/static/photos/%s.jpg' % (basepath, timestamp)
    camera.hflip = camera.vflip = False
    camera.resolution = (640, 400)
    camera.capture(photo_path)
    # send notification
    t = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
    msg = "HomeHZ: something append at " + t
    notificator.senddmimg(dest='fedehernandez', msg=msg, imgpath=photo_path)
    time.sleep(600)

