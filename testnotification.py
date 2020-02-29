from notification import TwNotificator
import time,os

t = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
msg = "HomeHZ: something append at " + t
path = os.path.dirname(os.path.realpath(__file__))
imgtest='%s/static/photos/test.jpg' % path

notificator = TwNotificator()
#notificator.senddm(dest='fedehernandez',msg=msg)
notificator.senddmimg(dest='fedehernandez',msg=msg,imgpath=imgtest)
