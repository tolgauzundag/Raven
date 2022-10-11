import pyrebase
import time
from requests.packages.urllib3.contrib.appengine import is_appengine_sandbox


print("Succes")
#time.sleep(10)
if is_appengine_sandbox():
    pass