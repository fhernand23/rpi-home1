import dropbox
from auth_dbox import (dropbox_access_key, dropbox_access_secret, dropbox_access_token)
import http.client as http_client

http_client.HTTPConnection.debuglevel = 1

dropbox_path= "/dog2.jpg"
local_path="./dog1.jpg"

client = dropbox.Dropbox(dropbox_access_token)
print("[SUCCESS] dropbox account linked")

client.files_upload(open(local_path, "rb").read(), dropbox_path)
print("[UPLOADED] {}".format(local_path))
