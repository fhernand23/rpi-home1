from flask import Flask, render_template
from picamera import PiCamera
from glob import glob
from datetime import datetime
import os
from flask import request
from homedb import HomeDB
from notification import TwNotificator
from irsensor import IrSensor


app = Flask(__name__)

path = os.path.dirname(os.path.realpath(__file__))
DBFILENAME = "./db.json"
KEY_APP_STATUS = "APP_STATUS"
KEY_SENSOR_IR_STATUS = "SENSOR_IR_STATUS"
# database
hdb = HomeDB(DBFILENAME)
# create notificator
notificator = TwNotificator()
# create ir sensor
# camera = PiCamera()
# irsensor = IrSensor(basepath=path, camera=camera)


def get_photos():
    photo_files = glob("%s/static/photos/*.jpg" % path)
    photos = ["/static/photos/%s" % photo.split('/')[-1] for photo in photo_files]
    return sorted(photos, reverse=True)


@app.route('/')
def index():
    photos = get_photos()
    app_status = hdb.get(KEY_APP_STATUS)
    ir_sensor_status = hdb.get(KEY_SENSOR_IR_STATUS)
    return render_template('index.html',
                           photos=photos,
                           app_status=app_status,
                           ir_sensor_status=ir_sensor_status)


@app.route('/capture/')
def capture():
    timestamp = datetime.now().isoformat()
    photo_path = '%s/static/photos/%s.jpg' % (path, timestamp)
    with PiCamera() as camera:
        camera.resolution = (640, 400)
        camera.capture(photo_path)
    return index()


@app.route('/view/<photo>/')
def view(photo):
    return render_template('view.html', photo=photo)


@app.route('/startir/')
def start_ir():
    # set sensor IR ON
    hdb.set(KEY_SENSOR_IR_STATUS, "ON")
    # irsensor.start(irstatus=hdb.get(KEY_SENSOR_IR_STATUS),notificator=notificator)
    return index()


@app.route('/stopir/')
def stop_ir():
    # set sensor IR OFF
    hdb.set(KEY_SENSOR_IR_STATUS, "OFF")
    # irsensor.stop()
    return index()


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


if __name__ == '__main__':
    # set app ON
    hdb.set(KEY_APP_STATUS, "OFF")
    # set sensor IR ON
    hdb.set(KEY_SENSOR_IR_STATUS, "OFF")
    # irsensor.start(irstatus=hdb.get(KEY_SENSOR_IR_STATUS),notificator=notificator)
    app.run(debug=True, host='0.0.0.0')
