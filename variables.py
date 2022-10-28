from pystyle import *
import pyrebase

firebaseConfig={ "apiKey": "AIzaSyC3fvl8ZWICyNWuHGkqPxTMRWnfOOKMhNk",
  "authDomain": "project-raven-c48d2.firebaseapp.com",
  "databaseURL": "https://project-raven-c48d2-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "project-raven-c48d2",
  "storageBucket": "project-raven-c48d2.appspot.com",
  "messagingSenderId": "176222167092",
  "appId": "1:176222167092:web:2edc8e1e5522e23be4ea61",
  "measurementId": "G-Z9QX5P2SJ5"}

uidsystem = {
  "apiKey": "AIzaSyCH5qwnuWCQVwdcE3Qbvz11I-9A0RMXi9s",
  "authDomain": "animated-flow-318519.firebaseapp.com",
  "databaseURL": "https://animated-flow-318519-default-rtdb.firebaseio.com",
  "projectId": "animated-flow-318519",
  "storageBucket": "animated-flow-318519.appspot.com",
  "messagingSenderId": "519430581076",
  "appId": "1:519430581076:web:6210e69583b6e7696c36c1"
};


firebasee=pyrebase.initialize_app(uidsystem)
dbsec=firebasee.database()
authsec=firebasee.auth()



text = r"""8888888b.         d8888 888     888 8888888888 888b    888 
888   Y88b       d88888 888     888 888        8888b   888 
888    888      d88P888 888     888 888        88888b  888 
888   d88P     d88P 888 Y88b   d88P 8888888    888Y88b 888 
8888888P"     d88P  888  Y88b d88P  888        888 Y88b888 
888 T88b     d88P   888   Y88o88P   888        888  Y88888 
888  T88b   d8888888888    Y888P    888        888   Y8888 
888   T88b d88P     888     Y8P     8888888888 888    Y888 



"""[:-1]
dark = Col.dark_gray
light = Col.light_gray
purple = Colors.StaticMIX((Col.purple, Col.blue))
green = Col.green
red = Col.red
bpurple = Colors.StaticMIX((Col.purple, Col.blue, Col.blue))
firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()
db=firebase.database()
close = "img/dwar/buttons/close.png"
cancel = "img/dwar/buttons/cancel.png"
win = "img/dwar/fight/win.png"
bear = "img/dwar/fight/bear.png"
milk = "img/dwar/fight/milk.png"
s1 = "img/dwar/fight/11.png"
s2 = "img/dwar/fight/22.png"
minimilk = "img/dwar/fight/minimilk.png"
coke = "img/dwar/fight/coke.png"
minicoke = "img/dwar/fight/minicoke.png"
fight = "img/global/vs.png"
map = "img/global/map.png"
sword = "img/global/sword.png"
closebutton = "img/dwar/buttons/quit.png"
####
test = "img/global/test.png"
test3 = "img/global/test3.png"


atk1 = "mid"
atk2 = "mid"
atk3 = "up"
atk4 = "down"
atk5 = "up"
atk6 = None
wincount=0

def stage(text: str, symbol: str = '...', col1=light, col2=None) -> str:
  if col2 is None:
    col2 = light if symbol == '...' else purple
  return f""" {Col.Symbol(symbol, col1, dark)} {col2}{text}{Col.reset}"""


def stagenormal(text: str, symbol: str = '...', col1=light, col2=None) -> str:
  if col2 is None:
    col2 = light if symbol == '...' else purple
  return f""" {Col.Symbol(symbol, col1, dark)} {col2}{text}{Col.reset}"""