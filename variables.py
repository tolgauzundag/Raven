from pystyle import *

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
blue = Col.blue
gray = Col.gray
bpurple = Colors.StaticMIX((Col.purple, Col.blue, Col.blue))
close = "img/dwar/buttons/close.png"
cancel = "img/dwar/buttons/cancel.png"
win = "img/dwar/fight/win2.png"
bear = "img/dwar/fight/bear.png"
milk = "img/dwar/fight/milk.png"
blueheal = "img/dwar/fight/blueheal.png"
greenheal = "img/dwar/fight/greenheal.png"
grayheal = "img/dwar/fight/grayheal.png"
mana = "img/dwar/fight/mana.png"
minimana = "img/dwar/fight/minimana.png"
s1 = "img/dwar/fight/11.png"
s2 = "img/dwar/fight/22.png"
step1 = "img/dwar/fight/exit.png"
minimilk = "img/dwar/fight/minimilk.png"
miniblueheal= "img/dwar/fight/blueminiheal.png"
minigreenheal = "img/dwar/fight/greenminiheal.png"
minigrayheal = "img/dwar/fight/grayminiheal.png"
coke = "img/dwar/fight/coke.png"
minicoke = "img/dwar/fight/minicoke.png"
fight = "img/global/vs.png"
map = "img/global/map.png"
sword = "img/global/sword2.png"
mage = "img/global/mage.png"
closebutton = "img/dwar/buttons/quit.png"
dead = "img/dwar/error/idead.png"
####
test = "img/global/test.png"
test3 = "img/global/test3.png"

aup = "img/dwar/fight/attackup.png"
amid = "img/dwar/fight/attackmid.png"
alow = "img/dwar/fight/attacklow.png"


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

