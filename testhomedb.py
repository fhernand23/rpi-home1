from homedb import HomeDB


DBFILENAME = "./db.json"
APP_STATUS = "APP_STATUS"
IR_SENSOR_STATUS = "IR_SENSOR_STATUS"

hdb = HomeDB(DBFILENAME)
hdb.set("APP_STATUS", "ON")
hdb.set(IR_SENSOR_STATUS, "ON")
print("APP_STATUS=" + str(hdb.get(APP_STATUS)))
print("IR_SENSOR_STATUS=" + str(hdb.get(IR_SENSOR_STATUS)))
