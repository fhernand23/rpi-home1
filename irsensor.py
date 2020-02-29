from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
import time


class IrSensor():
    def __init__(self, basepath, camera):
        self.basepath = basepath
        self.pir = MotionSensor(4)
        self.camera = camera

    def start(self, irstatus, notificator):
        if "ON"==irstatus:
            self.pir.wait_for_motion()
            print("Motion detected!")
            # take picture
            timestamp = datetime.now().isoformat()
            photo_path = '%s/static/photos/%s.jpg' % (self.basepath, timestamp)
            self.camera.hflip = self.camera.vflip = False
            self.camera.resolution = (640, 400)
            self.camera.capture(photo_path)
            # send notification
            t = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
            msg = "HomeHZ: something append at " + t
            notificator.senddmimg(dest='fedehernandez', msg=msg, imgpath=photo_path)
            time.sleep(600)

    def stop(self):
        self.pir.wait_for_no_motion()



