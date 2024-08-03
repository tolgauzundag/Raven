from pystyle import *
import pwinput
import time
from urllib.request import urlopen
import pickle
from variables import *
import pyautogui
import random
import cv2
import numpy as np
import datetime
import subprocess
import os


class Gui:
    def __init__(self):
        self.mob = "Krets(1)"
        self.version="1.0.2"
        self.mobpath = None
        self.pocket1 = None
        self.pocket2 = None
        self.pocket3 = None
        self.pocket4 = None
        self.pocket5 = None
        self.pocket6 = None
        self.pocket7 = None
        self.atk1 = "None"
        self.atk2 = "None"
        self.atk3 = "None"
        self.atk4 = "None"
        self.atk5 = "None"
        self.atk6 = "None"
        self.atk7 = "None"
        self.maxhunt = 400
        self.magelvl = "Kapalı"
        self.openblockstart = "None"
        self.openblockwhennopotion="None"
        self.potioncountblock = "None"
        self.potionblockonof = "None"
        self.endblockopen = "False"
        try:
            self.load()
        except:
            self.printer("Kayıt Dosyası Yuklenirken Hata Oluştu!!!")
            time.sleep(3)

    def pocketstring(self,pocket):
        if pocket == 1:
            if self.pocket1 is not None:
                x1 = "[1]Pocket1: " + self.pocket1
                return x1
            else:
                x1 = "[1]Pocket1: " + "None"
                return x1
        if pocket == 2:
            if self.pocket2 is not None:
                x1 = "[2]Pocket2: " + self.pocket2
                return x1
            else:
                x1 = "[2]Pocket2: " + "None"
                return x1
        if pocket == 3:
            if self.pocket3 is not None:
                x1 = "[3]Pocket3: " + self.pocket3
                return x1
            else:
                x1 = "[3]Pocket3: " + "None"
                return x1
        if pocket == 4:
            if self.pocket4 is not None:
                x1 = "[4]Pocket4: " + self.pocket4
                return x1
            else:
                x1 = "[4]Pocket4: " + "None"
                return x1
        if pocket == 5:
            if self.pocket5 is not None:
                x1 = "[5]Pocket5: " + self.pocket5
                return x1
            else:
                x1 = "[5]Pocket5: " + "None"
                return x1
        if pocket == 6:
            if self.pocket6 is not None:
                x1 = "[6]Pocket6: " + self.pocket6
                return x1
            else:
                x1 = "[6]Pocket6: " + "None"
                return x1
        if pocket == 7:
            if self.pocket7 is not None:
                x1 = "[7]Pocket7: " + self.pocket7
                return x1
            else:
                x1 = "[7]Pocket7: " + "None"
                return x1

    def attackstring(self, pocket):
        if pocket == 1:
            if self.atk1 is not None:
                x1 = "[1]Attack1: " + self.atk1
                return x1
            else:
                x1 = "[1]Attack1: " + "None"
                return x1
        if pocket == 2:
            if self.atk2 is not None:
                x1 = "[2]Attack2: " + self.atk2
                return x1
            else:
                x1 = "[2]Attack2: " + "None"
                return x1
        if pocket == 3:
            if self.atk3 is not None:
                x1 = "[3]Attack3: " + self.atk3
                return x1
            else:
                x1 = "[3]Attack3: " + "None"
                return x1
        if pocket == 4:
            if self.atk4 is not None:
                x1 = "[4]Attack4: " + self.atk4
                return x1
            else:
                x1 = "[4]Attack4: " + "None"
                return x1
        if pocket == 5:
            if self.atk5 is not None:
                x1 = "[5]Attack5: " + self.atk5
                return x1
            else:
                x1 = "[5]Attack5: " + "None"
                return x1
        if pocket == 6:
            if self.atk6 is not None:
                x1 = "[6]Attack6: " + self.atk6
                return x1
            else:
                x1 = "[6]Attack6: " + "None"
                return x1
        if pocket == 7:
            if self.atk7 is not None:
                x1 = "[7]Attack7: " + self.atk7
                return x1
            else:
                x1 = "[7]Attack7: " + "None"
                return x1

    def mainscreen(self):
        while True:
            self.checktimeleft()
            self.save()
            print(Colorate.Diagonal(Colors.DynamicMIX((green, Col.black)), Center.XCenter(text)))
            print('\n')
            # print(stagenormal(f"Sürüm 0.0.4 {Col.reset}", "!", col2=green))
            welcome = "Hosgeldin!"
            print(stagenormal(welcome, "!", col2=green))
            timeleft = "Kalan : " + str(self.time)+" Gun"
            print(stagenormal(timeleft, "!", col2=green))

            print('\n')
            mobguitext = Colorate.Color(Colors.green, "[1]Yaratik :", True, )
            self.mobcoloredprint = Colorate.Color(Colors.red, self.mob, True, )
            print(mobguitext+" "+self.mobcoloredprint)
            print(Colorate.Color(Colors.green, "[2]Pot Ayarlari", True, ))
            print(Colorate.Color(Colors.green, "[3]Avlanma Ve Savas Ayarlari", True, ))
            print(Colorate.Color(Colors.green, "[baslat]Botu Baslat", True, ))
            print(Colorate.Color(Colors.green, "[kapat]Botu Kapat", True, ))
            x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
            if x == "1":
                self.blank()
                self.moblvlselect()
            elif x == "2":
                self.potionsettings()
            elif x == "3":
                self.huntsettings()
            elif x == "k":
                exit(1)
            elif x == "g":
                exit(1)
            elif x == "k":
                exit(1)
            elif x == "back":
                exit(1)
            elif x == "kapat":
                exit(1)
            elif x == "baslat":
                script = MainProcess()
                script.start()

    def huntsettings(self):
        while True:
            self.blank()
            self.save()
            c = "[1]Hunt_Limit: " + str(self.maxhunt)
            #blocktext = "[3]Block_Setting: " + str(self.maxhunt)
            c2 = "[3]Büyücü: " + str(self.magelvl)
            print(Colorate.Color(Colors.green, c, True, ))
            print(Colorate.Color(Colors.green, "[2]Super_Attack_Settings ", True, ))
            print(Colorate.Color(Colors.green, "[3]Block_Settings", True, ))
            print(Colorate.Color(Colors.green, "[exit]Back", True, ))
            x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                print(Colorate.Color(Colors.purple, "Changing Variable!", True, ))
                try:
                    x = input(stage(f"Enter (NUMBER) : {dark}-> {Col.reset}", "?", col2=bpurple))
                    x = int(x)
                    self.maxhunt = x
                except:
                    print(Colorate.Color(Colors.purple, "Please enter number only!", True, ))
                    time.sleep(2)
            elif x == "2":
                self.superattack()
                return
            elif x == "3":
                self.blocksettings()
            elif x == "4":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_yellow, "[1]True", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]False", 1))
                x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.magelvl = "Açık"
                elif x == "2":
                    self.magelvl = "Kapalı"
            elif x == "g":
                return "exit"
            elif x == "k":
                return "exit"
            elif x == "back":
                return "exit"
            elif x == "b":
                return "exit"
            elif x == "exit":
                return "exit"

    def blocksettings(self):
        while True:
            self.blank()
            c = "[1]Block_Activation_Settings" + str(self.endblockopen)
            print(Colorate.Color(Colors.green, c, True, ))
            x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                while True:
                    self.blank()
                    print1 = "[1]Activate_Block_When_Fight_Begins: " + str(self.openblockstart)
                    print2 = "[2]Activate_Block_When_No_Potion_Left: " + str(self.openblockwhennopotion)
                    print3 = "[3]Activate_Block_When_Used_" + str(self.potioncountblock) + "_Heal_Potions: " + str(
                        self.potionblockonof)
                    print4 = "[4]Activate_Block_When_Enemy_Count_>1: " + str(self.endblockopen)
                    print(Colorate.Color(Colors.green, print1, True, ))
                    print(Colorate.Color(Colors.green, print2, True, ))
                    print(Colorate.Color(Colors.green, print3, True, ))
                    print(Colorate.Color(Colors.green, print4, True, ))
            elif x == "1":
                if self.openblockstart == "None":
                    self.openblockstart = "True"
                else:
                    self.openblockstart = "None"
            elif x == "2":
                if self.openblockwhennopotion == "None":
                    self.openblockwhennopotion = "True"
                else:
                    self.openblockwhennopotion = "None"
            elif x == "3":
                self.blank()
                print(Colorate.Color(Colors.green, "[1]Change_Potion_Count", True, ))
                print(Colorate.Color(Colors.green, "[2]Enable_Or_Disable_Function", True, ))
                x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)

                if x == "1":
                    print(Colorate.Color(Colors.purple, "Changing Variable!", True, ))
                    try:
                        x = input(stage(f"Enter Potion (NUMBER) : {dark}-> {Col.reset}", "?", col2=bpurple))
                        x = int(x)
                        self.potioncountblock = x
                    except:
                        print(Colorate.Color(Colors.purple, "Please enter number only!", True, ))
                        time.sleep(2)
                elif x == "2":
                    if self.potionblockonof == "False":
                        pass

    def superattack(self):
        while True:
            self.blank()
            self.save()
            print(Colorate.Color(Colors.green, self.attackstring(1), True, ))
            print(Colorate.Color(Colors.green, self.attackstring(2), True, ))
            print(Colorate.Color(Colors.green, self.attackstring(3), True, ))
            print(Colorate.Color(Colors.green, self.attackstring(4), True, ))
            print(Colorate.Color(Colors.green, self.attackstring(5), True, ))
            print(Colorate.Color(Colors.green, self.attackstring(6), True, ))
            print(Colorate.Color(Colors.green, self.attackstring(7), True, ))
            print(Colorate.Color(Colors.green, "[exit]Back", True, ))
            x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_yellow, "[1]Up", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Mid", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[3]Down", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[4]None", 1))
                x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.atk1 = "Up"
                elif x == "2":
                    self.atk1 = "Mid"
                elif x == "3":
                    self.atk1 = "Down"
                elif x == "4":
                    self.atk1 = "None"
            elif x == "2":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_yellow, "[1]Up", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Mid", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[3]Down", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[4]None", 1))
                x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.atk2 = "Up"
                elif x == "2":
                    self.atk2 = "Mid"
                elif x == "3":
                    self.atk2 = "Down"
                elif x == "4":
                    self.atk2 = "None"
            elif x == "3":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_yellow, "[1]Up", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Mid", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[3]Down", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[4]None", 1))
                x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.atk3 = "Up"
                elif x == "2":
                    self.atk3 = "Mid"
                elif x == "3":
                    self.atk3 = "Down"
                elif x == "4":
                    self.atk3 = "None"
            elif x == "4":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_yellow, "[1]Up", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Mid", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[3]Down", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[4]None", 1))
                x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.atk4 = "Up"
                elif x == "2":
                    self.atk4 = "Mid"
                elif x == "3":
                    self.atk4 = "Down"
                elif x == "4":
                    self.atk4 = "None"
            elif x == "5":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_yellow, "[1]Up", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Mid", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[3]Down", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[4]None", 1))
                x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.atk5 = "Up"
                elif x == "2":
                    self.atk5 = "Mid"
                elif x == "3":
                    self.atk5 = "Down"
                elif x == "4":
                    self.atk5 = "None"
            elif x == "6":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_yellow, "[1]Up", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Mid", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[3]Down", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[4]None", 1))
                x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.atk6 = "Up"
                elif x == "2":
                    self.atk6 = "Mid"
                elif x == "3":
                    self.atk6 = "Down"
                elif x == "4":
                    self.atk6 = "None"
            elif x == "7":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_yellow, "[1]Up", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Mid", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[3]Down", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[4]None", 1))
                x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.atk7 = "Up"
                elif x == "2":
                    self.atk7 = "Mid"
                elif x == "3":
                    self.atk7 = "Down"
                elif x == "4":
                    self.atk7 = "None"
            elif x == "g":
                return "exit"
            elif x == "k":
                return "exit"
            elif x == "back":
                return "exit"
            elif x == "b":
                return "exit"
            elif x == "exit":
                return "exit"

    def moblvlselect(self):
        while True:
            self.blank()
            print(Colorate.Color(Colors.green, "[1]Seviye 1 Yaratiklar", True, ))
            print(Colorate.Color(Colors.green, "[2]Seviye 2 Yaratiklar", True, ))
            print(Colorate.Color(Colors.green, "[3]Seviye 3 Yaratiklar", True, ))
            print(Colorate.Color(Colors.green, "[4]Seviye 4 Yaratiklar", True, ))
            print(Colorate.Color(Colors.green, "[5]Seviye 5 Yaratiklar", True, ))
            print(Colorate.Color(Colors.green, "[6]Seviye 6 Yaratiklar", True, ))
            print(Colorate.Color(Colors.green, "[7]Seviye 7 Yaratiklar", True, ))
            print(Colorate.Color(Colors.green, "[8]Seviye 8 Yaratiklar", True, ))
            print(Colorate.Color(Colors.green, "[9]Seviye 9 Yaratiklar", True, ))
            print(Colorate.Color(Colors.green, "[10]Seviye 10 Yaratiklar", True, ))
            print(Colorate.Color(Colors.green, "[exit]Main Menu", True, ))
            x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.blank()
                self.lvl1mobs()
                return x
            elif x == "2":
                self.blank()
                self.lvl2mobs()
                return x
            elif x == "3":
                self.blank()
                self.lvl3mobs()
                return x
            elif x == "4":
                self.blank()
                self.lvl4mobs()
                return x
            elif x == "5":
                self.blank()
                self.lvl5mobs()
                return x
            elif x == "6":
                self.blank()
                self.lvl6mobs()
                return x
            elif x == "7":
                self.blank()
                self.lvl7mobs()
                return x
            elif x == "8":
                self.blank()
                self.lvl8mobs()
                return x
            elif x == "9":
                self.blank()
                self.lvl9mobs()
                return
            elif x == "10":
                self.blank()
                self.lvl10mobs()
                return x
            elif x == "g":
                return "exit"
            elif x == "k":
                return "exit"
            elif x == "back":
                return "exit"
            elif x == "b":
                return "exit"
            elif x == "exit":
                return "exit"

    def lvl1mobs(self):
        while True:
            self.blank()
            print(Colorate.Color(Colors.green, "[1]Krets(1)", True, ))
            print(Colorate.Color(Colors.green, "[2]Deli Kopek(1)", True, ))
            print(Colorate.Color(Colors.green, "[k]Ana Menu", True, ))
            x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.mob = "Krets(1)"
                self.mobpath = "img/dwar/mobs/1Level/krets.png"
                return x
            elif x == "2":
                self.mob = "Deli Kopek(1)"
                self.mobpath = "img/dwar/mobs/1Level/delikopek.png"
                return x
            elif x == "g":
                return "exit"
            elif x == "k":
                return "exit"
            elif x == "back":
                return "exit"
            elif x == "b":
                return "exit"
            elif x == "exit":
                return "exit"

    def lvl2mobs(self):
        while True:
            self.blank()
            print(Colorate.Color(Colors.green, "[1]Yasli Iskelet(2)", True, ))
            print(Colorate.Color(Colors.green, "[2]Erkek Ates Orumcegi(2)", True, ))
            print(Colorate.Color(Colors.green, "[3]Krets Lideri(2)", True, ))
            print(Colorate.Color(Colors.green, "[4]Kuduz Kopek(2)", True, ))
            print(Colorate.Color(Colors.green, "[k]Ana Menu", True, ))
            x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.mob = "Yasli Iskelet(2)"
                self.mobpath = "img/dwar/mobs/2Level/yasli.png"
                return x
            elif x == "2":
                self.mob = "Erkek Ates Orumcegi(2)"
                self.mobpath = "img/dwar/mobs/2Level/erkekates.png"
                return x
            elif x == "3":
                self.mob = "Krets Lideri(2)"
                self.mobpath = "img/dwar/mobs/2Level/kretslideri.png"
                return x
            elif x == "4":
                self.mob = "Kuduz Kopek(2)"
                self.mobpath = "img/dwar/mobs/2Level/kuduzkopek.png"
                return x
            elif x == "g":
                return "exit"
            elif x == "k":
                return "exit"
            elif x == "back":
                return "exit"
            elif x == "b":
                return "exit"
            elif x == "exit":
                return "exit"

    def lvl3mobs(self):
        while True:
            self.blank()
            print(Colorate.Color(Colors.green, "[1]Azgin Kopek(3)", True, ))
            print(Colorate.Color(Colors.green, "[2]Reis Krets(3)", True, ))
            print(Colorate.Color(Colors.green, "[3]Disi Ates Orumcegi(3)", True, ))
            print(Colorate.Color(Colors.green, "[4]Savasci Zigred(3)", True, ))
            print(Colorate.Color(Colors.green, "[5]Savasci_Iskelet(3)", True, ))
            print(Colorate.Color(Colors.green, "[6]Erkek Kul Orumcegi(3)", True, ))
            print(Colorate.Color(Colors.green, "[k]Ana Menu", True, ))
            x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.mob = "Azgin Kopek(3)"
                self.mobpath = "img/dwar/mobs/3Level/azginkopek.png"
                return x
            elif x == "2":
                self.mob = "Reis Krets(3)"
                self.mobpath = "img/dwar/mobs/3Level/reiskrets.png"
                return x
            elif x == "3":
                self.mob = "Disi Ates Orumcegi(3)"
                self.mobpath = "img/dwar/mobs/3Level/disiates.png"
                return x
            elif x == "4":
                self.mob = "Savasci Zigred(3)"
                self.mobpath = "img/dwar/mobs/3Level/savascizigred.png"
                return x
            elif x == "5":
                self.mob = "Savasci Iskelet(3)"
                self.mobpath = "img/dwar/mobs/3Level/savasciiskelet.png"
                return x
            elif x == "6":
                self.mob = "Erkek Kul Orumcegi(3)"
                self.mobpath = "img/dwar/mobs/3Level/erkekkul.png"
                return x
            elif x == "g":
                return "exit"
            elif x == "k":
                return "exit"
            elif x == "back":
                return "exit"
            elif x == "b":
                return "exit"
            elif x == "exit":
                return "exit"

    def lvl4mobs(self):
        while True:
            self.blank()
            print(Colorate.Color(Colors.green, "[1]Yasli Cin Kopek(4)", True, ))
            print(Colorate.Color(Colors.green, "[2]Erguvani Zigred(4)", True, ))
            print(Colorate.Color(Colors.green, "[3]Kocaman Zigred(4)", True, ))
            print(Colorate.Color(Colors.green, "[4]Zombi(4)", True, ))
            print(Colorate.Color(Colors.green, "[5]Hakurt(4)", True, ))
            print(Colorate.Color(Colors.green, "[6]Genc Oduni(4)", True, ))
            print(Colorate.Color(Colors.green, "[7]Young_Berona_Tiger(4)", True, ))
            print(Colorate.Color(Colors.green, "[8]Cunning_Phitzell(4)", True, ))
            print(Colorate.Color(Colors.green, "[9]Arboris(4)", True, ))
            print(Colorate.Color(Colors.green, "[10]Veteran_Berona_Tiger(4)", True, ))
            print(Colorate.Color(Colors.green, "[11]Ice_Kakurt(4)", True, ))
            print(Colorate.Color(Colors.green, "[12]Krogan(4)", True, ))
            print(Colorate.Color(Colors.green, "[k]Ana Menu", True, ))
            x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.mob = "Yasli Cin Kopek(4)"
                self.mobpath = "img/dwar/mobs/4Level/yaslicin.png"
                return x
            elif x == "2":
                self.mob = "Erguvani Zigred(4)"
                self.mobpath = "img/dwar/mobs/4Level/erguvanizigred.png"
                return x
            elif x == "3":
                self.mob = "Kocaman Zigred(4)"
                self.mobpath = "img/dwar/mobs/4Level/kocamanzigred.png"
                return x
            elif x == "4":
                self.mob = "Zombi(4)"
                self.mobpath = "img/dwar/mobs/4Level/zombi.png"
                return x
            elif x == "5":
                self.mob = "Hakurt(4)"
                self.mobpath = "img/dwar/mobs/4Level/hakurt.png"
                return x
            elif x == "6":
                self.mob = "Genc Oduni(4)"
                self.mobpath = "img/dwar/mobs/4Level/gencoduni.png"
                return x
            elif x == "7":
                self.mob = "Young_Berona_Tiger(4)"
                self.mobpath = "img/warof/mobs/4Level/Young_Berona_Tiger.png"
                return x
            elif x == "8":
                self.mob = "Cunning_Phitzell(4)"
                self.mobpath = "img/warof/mobs/4Level/Cunning_Phitzell.png"
                return x
            elif x == "9":
                self.mob = "Arboris(4)"
                self.mobpath = "img/warof/mobs/4Level/Arboris.png"
                return True
            elif x == "10":
                self.mob = "Veteran_Berona_Tiger(4)"
                self.mobpath = "img/warof/mobs/4Level/Veteran_Berona_Tiger.png"
                return True
            elif x == "11":
                self.mob = "Ice_Kakurt(4)"
                self.mobpath = "img/warof/mobs/4Level/Ice_Kakurt.png"
                return True
            elif x == "12":
                self.mob = "Krogan(4)"
                self.mobpath = "img/warof/mobs/4Level/Krogan.png"
                return True
            elif x == "g":
                return "exit"
            elif x == "k":
                return "exit"
            elif x == "back":
                return "exit"
            elif x == "b":
                return "exit"
            elif x == "exit":
                return "exit"

    def lvl5mobs(self):
        while True:
            self.blank()
            print(Colorate.Color(Colors.green, "[1]Duarkharq(5)", True, ))
            print(Colorate.Color(Colors.green, "[2]Pkhadd_Bear(5)", True, ))
            print(Colorate.Color(Colors.green, "[3]Forest_Iguraon(5)", True, ))
            print(Colorate.Color(Colors.green, "[4]Maverick_Gungl(5)", True, ))
            print(Colorate.Color(Colors.green, "[5]Blood-Sucking_Zigred(5)", True, ))
            print(Colorate.Color(Colors.green, "[6]Vampire(5)", True, ))
            print(Colorate.Color(Colors.green, "[7]Liche(5)", True, ))
           #print(Colorate.Color(Colors.green, "[8]Cin Köpek İskeleti(5)", True, ))
            print(Colorate.Color(Colors.green, "[9]Orc_Conauistador_Skleleton(5)", True, ))
            print(Colorate.Color(Colors.green, "[10]Stone_Lotus_Outcast(5)", True, ))
            print(Colorate.Color(Colors.green, "[11]Red_Axes_Outcast(5)", True, ))
            print(Colorate.Color(Colors.green, "[exit]Main Menu", True, ))
            x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.mob = "Duarkharq(5)"
                self.mobpath = "img/warof/mobs/5Level/Duarkharq.png"
                return True
            elif x == "2":
                self.mob = "Pkhadd_Bear(5)"
                self.mobpath = "img/warof/mobs/5Level/Pkhadd_Bear.png"
                return True
            elif x == "3":
                self.mob = "Forest_Iguraon(5)"
                self.mobpath = "img/warof/mobs/5Level/Forest_Iguraon.png"
                return True
            elif x == "4":
                self.mob = "Maverick_Gungl(5)"
                self.mobpath = "img/warof/mobs/5Level/Maverick_Gungl.png"
                return True

            elif x == "5":
                self.mob = "Blood-Sucking_Zigred(5)"
                self.mobpath = "img/warof/mobs/5Level/Blood-Sucking_Zigred.png"
                return True

            elif x == "6":
                self.mob = "Vampire(5)"
                self.mobpath = "img/warof/mobs/5Level/Vampire.png"
                return True

            elif x == "7":
                self.mob = "Liche(5)"
                self.mobpath = "img/warof/mobs/5Level/Liche.png"
                return True
            elif x == "8":
                self.mob = "Cin Köpek İskeleti(5)"
                self.mobpath = "img/warof/mobs/5Level/.png"

            elif x == "9":
                self.mob = "Orc_Conauistador_Skleleton(5)"
                self.mobpath = "img/warof/mobs/5Level/Orc_Conauistador_Skleleton.png"
                return True
            elif x == "10":
                self.mob = "Stone_Lotus_Outcast(5)"
                self.mobpath = "img/warof/mobs/5Level/Stone_Lotus_Outcast.png"
                return True
            elif x == "11":
                self.mob = "Red_Axes_Outcast(5)"
                self.mobpath = "img/warof/mobs/5Level/Red_Axes_Outcast.png"
                return True
            elif x == "g":
                return "exit"
            elif x == "k":
                return "exit"
            elif x == "back":
                return "exit"
            elif x == "b":
                return "exit"
            elif x == "exit":
                return "exit"

    def lvl6mobs(self):
        while True:
            self.blank()
            print(Colorate.Color(Colors.green, "[1]Veteran_Durgkhang(6)", True, ))
            print(Colorate.Color(Colors.green, "[2]Kodrag(6)", True, ))
            print(Colorate.Color(Colors.green, "[3]Old_Pkhadd_Bear(6)", True, ))
            print(Colorate.Color(Colors.green, "[4]Gordt(6)", True, ))
            print(Colorate.Color(Colors.green, "[5]Clay_Golem(6)", True, ))
           #print(Colorate.Color(Colors.green, "[6]GungIDO(6)", True, ))
           #print(Colorate.Color(Colors.green, "[7]Rukkub İskeleti(6)", True, ))
            print(Colorate.Color(Colors.green, "[8]Stone_Lotus_Renegade(6)", True, ))
           #print(Colorate.Color(Colors.green, "[9]Levremar Askeri(6)", True, ))
            print(Colorate.Color(Colors.green, "[10]Red_Axes_Reneoadel(6)", True, ))
            print(Colorate.Color(Colors.green, "[11]Atshi_Bat(6)", True, ))
            print(Colorate.Color(Colors.green, "[exit]Main Menu", True, ))
            x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.mob = "Veteran_Durgkhang(6)"
                self.mobpath = "img/warof/mobs/6Level/Veteran_Durgkhang.png"
                return True
            elif x == "2":
                self.mob = "Kodrag(6)"
                self.mobpath = "img/warof/mobs/6Level/Kodrag.png"
                return True
            elif x == "3":
                self.mob = "Old_Pkhadd_Bear(6)"
                self.mobpath = "img/warof/mobs/6Level/Old_Pkhadd_Bear.png"
                return True
            elif x == "4":
                self.mob = "Gordt(6)"
                self.mobpath = "img/warof/mobs/6Level/Gordt.png"
                return True
            elif x == "5":
                self.mob = "Clay_Golem(6)"
                self.mobpath = "img/warof/mobs/6Level/Clay_Golem.png"
                return True
            elif x == "6":
                self.mob = "GungIDO(6)"
                self.mobpath = "img/warof/mobs/6Level/.png"
                return True
            elif x == "7":
                self.mob = "Rukkub İskeleti(6)"
                self.mobpath = "img/warof/mobs/6Level/.png"
                return True
            elif x == "8":
                self.mob = "Stone_Lotus_Renegade(6)"
                self.mobpath = "img/warof/mobs/6Level/Stone_Lotus_Renegade.png"
                return True
            elif x == "9":
                self.mob = "Levremar Askeri(6)"
                self.mobpath = "img/warof/mobs/6Level/.png"
                return True
            elif x == "10":
                self.mob = "Red_Axes_Reneoadel(6)"
                self.mobpath = "img/warof/mobs/6Level/Red_Axes_Reneoadel.png"
                return True
            elif x == "11":
                self.mob = "Atshi_Bat(6)"
                self.mobpath = "img/warof/mobs/6Level/Atshi_Bat.png"
                return True
            elif x == "g":
                return "exit"
            elif x == "k":
                return "exit"
            elif x == "back":
                return "exit"
            elif x == "b":
                return "exit"
            elif x == "exit":
                return "exit"

    def lvl7mobs(self):
        while True:
            self.blank()
           #print(Colorate.Color(Colors.green, "[1]Levremar Lejyoneri(7)", True, ))
            print(Colorate.Color(Colors.green, "[2]Young_Valdagor_Wolf(7)", True, ))
            print(Colorate.Color(Colors.green, "[3]Valdagor_Wolf(7)", True, ))
            print(Colorate.Color(Colors.green, "[4]Gordt_Bandit(7)", True, ))
            print(Colorate.Color(Colors.green, "[5]Stone_Golem(7)", True, ))
            print(Colorate.Color(Colors.green, "[6]Saber-tooth_Tiger(7)", True, ))
            print(Colorate.Color(Colors.green, "[7]Lame Saber-tooth_Tiger(7)", True, ))
           #print(Colorate.Color(Colors.green, "[8]GungIVO(7)", True, ))
            print(Colorate.Color(Colors.green, "[exit]Main Menu", True, ))
            x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.mob = "Levremar Lejyoneri(7)"
                self.mobpath = "img/warof/mobs/7Level/.png"
                return True
            elif x == "2":
                self.mob = "Young_Valdagor_Wolf(7)"
                self.mobpath = "img/warof/mobs/7Level/Young_Valdagor_Wolf.png"
                return True
            elif x == "3":
                self.mob = "Valdagor_Wolf(7)"
                self.mobpath = "img/warof/mobs/7Level/Valdagor_Wolf.png"
                return True
            elif x == "4":
                self.mob = "Gordt_Bandit(7)"
                self.mobpath = "img/warof/mobs/7Level/Gordt_Bandit.png"
                return True
            elif x == "5":
                self.mob = "Stone_Golem(7)"
                self.mobpath = "img/warof/mobs/7Level/Stone_Golem.png"
                return True
            elif x == "6":
                self.mob = "Saber-tooth_Tiger(7)"
                self.mobpath = "img/warof/mobs/7Level/Saber-tooth_Tiger.png"
                return True
            elif x == "7":
                self.mob = "Lame Saber-tooth_Tiger(7)"
                self.mobpath = "img/warof/mobs/7Level/Lame Saber-tooth_Tiger.png"
                return True
            elif x == "8":
                self.mob = "GungIVO(7)"
                self.mobpath = "img/warof/mobs/7Level/.png"
                return True
            elif x == "g":
                return "exit"
            elif x == "k":
                return "exit"
            elif x == "back":
                return "exit"
            elif x == "b":
                return "exit"
            elif x == "exit":
                return "exit"

    def lvl8mobs(self):
        while True:
            self.blank()
            print(Colorate.Color(Colors.green, "[1]Gordt_Cutthroat(8)", True, ))
            print(Colorate.Color(Colors.green, "[2]Gargolye(8)", True, ))
            #print(Colorate.Color(Colors.green, "[3]Beyaz Ayı(8)", True, ))
            #print(Colorate.Color(Colors.green, "[4]Eşkiya Yeti Hantu(8)", True, ))
            #print(Colorate.Color(Colors.green, "[5]Keşifçi Yeti Yukari(8)", True, ))
            print(Colorate.Color(Colors.green, "[6]Granite_Golem(8)", True, ))
            #print(Colorate.Color(Colors.green, "[7]GungHO(8)", True, ))
            print(Colorate.Color(Colors.green, "[exit]Main Menu", True, ))
            x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.mob = "Gordt_Cutthroat(8)"
                self.mobpath = "img/warof/mobs/8Level/Gordt_Cutthroat.png"
                return True
            elif x == "2":
                self.mob = "Gargolye(8)"
                self.mobpath = "img/warof/mobs/8Level/Gargolye.png"
                return True
            elif x == "3":
                self.mob = "Beyaz Ayı(8)"
                self.mobpath = "img/warof/mobs/8Level/.png"
                return True
            elif x == "4":
                self.mob = "Eşkiya Yeti Hantu(8)"
                self.mobpath = "img/warof/mobs/8Level/.png"
                return True
            elif x == "5":
                self.mob = "Keşifçi Yeti Yukari(8)"
                self.mobpath = "img/warof/mobs/8Level/.png"
                return True
            elif x == "6":
                self.mob = "Granite_Golem(8)"
                self.mobpath = "img/warof/mobs/8Level/Granite_Golem.png"
                return True
            elif x == "7":
                self.mob = "GungHO(8)"
                self.mobpath = "img/warof/mobs/8Level/.png"
                return True

            elif x == "g":
                return "exit"
            elif x == "k":
                return "exit"
            elif x == "back":
                return "exit"
            elif x == "b":
                return "exit"
            elif x == "exit":
                return "exit"

    def lvl9mobs(self):
        while True:
            self.blank()
            print(Colorate.Color(Colors.green, "[1]Grim_Gargolye(9)", True, ))
            #print(Colorate.Color(Colors.green, "[2]Avcı Yeti Hantu(9)", True, ))
            #print(Colorate.Color(Colors.green, "[3]Zararcı Yeti Yukari(9)", True, ))
            #print(Colorate.Color(Colors.green, "[4]Vahşi Buz Ayısı(9)", True, ))
            #print(Colorate.Color(Colors.green, "[5]Gardiyan GungHO(9)", True, ))
            print(Colorate.Color(Colors.green, "[6]Large_Scorpion(9)", True, ))
            print(Colorate.Color(Colors.green, "[exit]Main Menu", True, ))
            x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.mob = "Grim_Gargolye(9)"
                self.mobpath = "img/warof/mobs/9Level/Grim_Gargolye.png"
                return True
            elif x == "2":
                self.mob = "Avcı Yeti Hantu(9)"
                self.mobpath = "img/warof/mobs/9Level/.png"
                return True
            elif x == "3":
                self.mob = "Zararcı Yeti Yukari(9)"
                self.mobpath = "img/warof/mobs/9Level/.png"
                return True
            elif x == "4":
                self.mob = "Vahşi Buz Ayısı(9)"
                self.mobpath = "img/warof/mobs/9Level/.png"
                return True
            elif x == "5":
                self.mob = "Gardiyan GungHO(9)"
                self.mobpath = "img/warof/mobs/9Level/.png"
            elif x == "6":
                self.mob = "Large_Scorpion(9)"
                self.mobpath = "img/warof/mobs/9Level/Large_Scorpion.png"
                return True
            elif x == "g":
                return "exit"
            elif x == "k":
                return "exit"
            elif x == "back":
                return "exit"
            elif x == "b":
                return "exit"
            elif x == "exit":
                return "exit"

    def lvl10mobs(self):
        while True:
            self.blank()
            print(Colorate.Color(Colors.green, "[1]King_Scorpion(10)", True, ))
            print(Colorate.Color(Colors.green, "[2]Fire_Kroffdor(10)", True, ))
            print(Colorate.Color(Colors.green, "[3]Eldive_Warrior(10)", True, ))
            print(Colorate.Color(Colors.green, "[exit]Main Menu", True, ))
            x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.mob = "King_Scorpion(10)"
                self.mobpath = "img/warof/mobs/9Level/Large_Scorpion.png"
                return True
            if x == "2":
                self.mob = "Fire_Kroffdor(10)"
                self.mobpath = "img/warof/mobs/9Level/Fire_Kroffdor.png"
                return True
            if x == "3":
                self.mob = "Eldive_Warrior(10)"
                self.mobpath = "img/warof/mobs/9Level/Eldive_Warrior.png"
                return True
            elif x == "g":
                return "exit"
            elif x == "k":
                return "exit"
            elif x == "back":
                return "exit"
            elif x == "b":
                return "exit"
            elif x == "exit":
                return "exit"

    def potionsettings(self):
        while True:
            self.blank()
            self.save()
            print(Colorate.Color(Colors.green, self.pocketstring(1), True, ))
            print(Colorate.Color(Colors.green, self.pocketstring(2), True, ))
            print(Colorate.Color(Colors.green, self.pocketstring(3), True, ))
            print(Colorate.Color(Colors.green, self.pocketstring(4), True, ))
            print(Colorate.Color(Colors.green, self.pocketstring(5), True, ))
            print(Colorate.Color(Colors.green, self.pocketstring(6), True, ))
            print(Colorate.Color(Colors.green, self.pocketstring(7), True, ))
            print(Colorate.Color(Colors.green, "[exit]Back", True, ))
            x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_red, "[1]Power", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Heal", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[3]Mana", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[4]None", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[5]Use At Start", 1))
                x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.pocket1 = "Power"
                elif x == "2":
                    self.pocket1 = "Heal"
                elif x == "3":
                    self.pocket1 = "Mana"
                elif x == "4":
                    self.pocket1 = "None"
                elif x == "5":
                    self.pocket1 = "Use At Start"

            elif x == "2":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_red, "[1]Power", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Heal", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[3]Mana", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[4]None", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[5]Use At Start", 1))
                x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.pocket2 = "Power"
                elif x == "2":
                    self.pocket2 = "Heal"
                elif x == "3":
                    self.pocket2 = "Mana"
                elif x == "4":
                    self.pocket2 = "None"
                elif x == "5":
                    self.pocket2 = "Use At Start"
            elif x == "3":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_red, "[1]Power", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Heal", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[3]Mana", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[4]None", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[5]Use At Start", 1))
                x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.pocket3 = "Power"
                elif x == "2":
                    self.pocket3 = "Heal"
                elif x == "3":
                    self.pocket3 = "Mana"
                elif x == "4":
                    self.pocket3 = "None"
                elif x == "5":
                    self.pocket3 = "Use At Start"
            elif x == "4":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_red, "[1]Power", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Heal", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[3]Mana", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[4]None", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[5]Use At Start", 1))
                x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.pocket4 = "Power"
                elif x == "2":
                    self.pocket4 = "Heal"
                elif x == "3":
                    self.pocket4 = "Mana"
                elif x == "4":
                    self.pocket4 = "None"
                elif x == "5":
                    self.pocket4 = "Use At Start"
            elif x == "5":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_red, "[1]Power", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Heal", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[3]Mana", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[4]None", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[5]Use At Start", 1))
                x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.pocket5 = "Power"
                elif x == "2":
                    self.pocket5 = "Heal"
                elif x == "3":
                    self.pocket5 = "Mana"
                elif x == "4":
                    self.pocket5 = "None"
                elif x == "5":
                    self.pocket5 = "Use At Start"

            elif x == "6":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_red, "[1]Power", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Heal", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[3]Mana", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[4]None", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[5]Use At Start", 1))
                x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.pocket6 = "Power"
                elif x == "2":
                    self.pocket6 = "Heal"
                elif x == "3":
                    self.pocket6 = "Mana"
                elif x == "4":
                    self.pocket6 = "None"
                elif x == "5":
                    self.pocket6 = "Use At Start"
            elif x == "7":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_red, "[1]Power", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Heal", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[3]Mana", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[4]None", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "[5]Use At Start", 1))
                x = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.pocket7 = "Power"
                elif x == "2":
                    self.pocket7 = "Heal"
                elif x == "3":
                    self.pocket7 = "Mana"
                elif x == "4":
                    self.pocket7 = "None"
                elif x == "5":
                    self.pocket7 = "Use At Start"
            elif x == "g":
                return "exit"
            elif x == "k":
                return "exit"
            elif x == "back":
                return "exit"
            elif x == "b":
                return "exit"
            elif x == "exit":
                return "exit"

    def blank(self):
        x = 0
        while x < 19:
            x += 1
            print('\n')

    def timecalculator(self, current, fdata):
        try:
            current = (current.replace("-", ""))
            current = (current.replace(" ", ""))
            current = (current.replace(":", ""))
            currentyear = (current[:4])
            currentmonth = (current[4:6])
            currentday = (current[6:8])
            #############################
            fdata = (fdata.replace("-", ""))
            fdata = (fdata.replace(" ", ""))
            fdata = (fdata.replace(":", ""))
            fdatayear = (fdata[:4])
            fdatamonth = (fdata[4:6])
            fdataday = (fdata[6:8])
            # fdatayear*=365
            # fdatamonth*=30

            date1 = datetime.datetime(int(currentyear), int(currentmonth), int(currentday))
            date2 = datetime.datetime(int(fdatayear), int(fdatamonth), int(fdataday))
            x = (date2 - date1)
            day = x.days
            if day <= 0:
                return None
            else:
                return day
        except:
            return None

    def authtries(self):
        try:
            self.userlog = auth.sign_in_with_email_and_password(self.Usernamea, self.Passworda)
            self.ID = self.Usernamea
            self.userlogsecond = authsec.sign_in_with_email_and_password(self.ID, self.Passworda)
        except:
            usernameaddgmail = self.Usernamea + "@gmail.com"
            try:
                self.userlog = auth.sign_in_with_email_and_password(usernameaddgmail, self.Passworda)
                self.ID = usernameaddgmail
                self.userlogsecond = authsec.sign_in_with_email_and_password(usernameaddgmail, self.Passworda)
            except:
                usernameaddhotmail = self.Usernamea + "@hotmail.com"
                try:
                    self.userlog = auth.sign_in_with_email_and_password(usernameaddhotmail, self.Passworda)
                    self.ID = usernameaddhotmail
                    self.userlogsecond = authsec.sign_in_with_email_and_password(usernameaddhotmail, self.Passworda)
                except:
                    print(stagenormal(f"Unknown Email Or Password {Col.reset}", "!", col2=red))
                    print(stagenormal(f"Try Again In 3 sec {Col.reset}", "!", col2=red))
                    time.sleep(3)
                    return 0
        return 1

    def checktimeleft(self):
        try:
            res = urlopen('http://just-the-time.appspot.com/')
            result = res.read().strip()
            result_str = result.decode('utf-8')
            current = (result_str)
            x = self.timecalculator(current, "2024-11-28 14:33:32")
            if x is None:
                print(stagenormal(f"Membership Expired Or Not Available! {Col.reset}", "!", col2=green))
                time.sleep(3)
                exit()
            else:
                self.time = x
                time.sleep(2)
                return 1
        except:
            print(stagenormal(f"ERR:412! {Col.reset}", "!", col2=green))
            time.sleep(3)
            exit()
            return 0

    def checkversion(self):
        versionn = db.child("Version").get(self.userlog['idToken'])
        versionn = (versionn.val())
        version=str(versionn["version"])
        if version !=self.version:
            print(stagenormal(f"Invalid Version Please Update!! {Col.reset}", "!", col2=green))
            time.sleep(3)
            return 0

    def security(self):
        if "@gmail.com" in self.ID:
            IDTEMP = self.ID.replace("@gmail.com", "")
        elif "@hotmail.com" in self.ID:
            IDTEMP = self.ID.replace("@hotmail.com", "")
        current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
        users = dbsec.child("User").get(self.userlogsecond['idToken'])
        value = (users.val())
        try:
            uuidvalue = str(value[IDTEMP])
        except:
            data = {IDTEMP: current_machine_id}
            dbsec.child("User").update({IDTEMP: current_machine_id},(self.userlogsecond['idToken']))
            print(stagenormal(f"Account Linked To Computer Succesfuly"
                              f" Try Logging In Again {Col.reset}", "!", col2=dark))
            time.sleep(3)
            return 0
        if uuidvalue == current_machine_id:
            print(stagenormal(f"Confirmed! {Col.reset}", "!", col2=green))
            return 1
        else:
            print(stagenormal(f"Unknown Computer!!! {Col.reset}", "!", col2=red))
            time.sleep(3)
            return 0

    def login(self):
        System.Size(75, 22)
        System.Title("Raven WarOfDragons(English) 1.0.2")
        Cursor.HideCursor()
        print(Colorate.Diagonal(Colors.DynamicMIX((green, Col.black)), Center.XCenter(text)))
        print(Colorate.Color(Colors.green,
                             "!!!While Writing Email You Dont Have To Add @gmail.com or @hotmail.com", True, ))
        print('\n')
        self.Usernamea = input(stage(f"Email : {dark}-> {Col.reset}", "?", col2=bpurple))
        self.Passworda = input(stage(f"Passowrd : {dark}-> {Col.reset}", "?", col2=bpurple))
        print(stagenormal(f"Logging in {Col.reset}", "!", col2=dark))
        x = self.authtries()
        if x == 0:
            print(3)
            return 0
        x = self.checktimeleft()
        if x == 0:
            print(2)
            return 0
        x = self.checkversion()
        if x == 0:
            print("1")
            return 0
        x = self.security()
        if x == 0:
            print("5")
            return 0
        return True

    def register(self):
        self.blank()
        print(Colorate.Color(Colors.green, "!!!Epostanizi Yanlis Girerseniz Geri Alamazsiniz!!!", True, ))
        print(Colorate.Color(Colors.green, "!!!Sifreniz Minimum 3 Harften Olusmali", True, ))
        print(Colorate.Color(Colors.green, "!!!Sadece Gmail Veya Hotmail Kullanabilirsiniz!!!", True, ))
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print(Colorate.Color(Colors.green, "[geri]Ana Menu", True, ))
        email = input(stage(f"Eposta : {dark}-> {Col.reset}", "?", col2=bpurple))
        if str(email) == "geri":
            return 0
        password = input(stage(f"Şifre : {dark}-> {Col.reset}", "?", col2=bpurple))
        if str(password) == "geri":
            return 0
        password2 = input(stage(f"Şifre Tekrar : {dark}-> {Col.reset}", "?", col2=bpurple))
        if str(password2) == "geri":
            return 0
        if password == password2:
            try:
                auth.create_user_with_email_and_password(email, password)
                authsec.create_user_with_email_and_password(email, password)
            except:
                print(Colorate.Color(Colors.green, "!Uyeliginizi Olusturken Bir Hata Olustu!",True, ))
                time.sleep(3)

    def paswordreset(self):
        self.blank()
        print(Colorate.Color(Colors.green, "!!!2 E-mails Will Be Sent To Your E-mail Address. Follow the 2 Links And En"
                                           "ter The Same Password.", True, ))
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print(Colorate.Color(Colors.green, "[exit]Main Menu", True, ))
        email = input(stage(f"Email : {dark}-> {Col.reset}", "?", col2=bpurple))
        if str(email) == "exit":
            return 0
        try:
            auth.send_password_reset_email(email)
            authsec.send_password_reset_email(email)
            print(Colorate.Color(Colors.green, "", True, ))
        except:
            print(Colorate.Color(Colors.green, "!Error!",True, ))

    def startmenu(self):
        while True:
            System.Title("Raven WarOfDragons(English) 1.0.2")
            System.Size(75, 22)
            Cursor.HideCursor()
            print(Colorate.Diagonal(Colors.DynamicMIX((green, Col.black)), Center.XCenter(text)))
            print(stagenormal(f"Logged In! {Col.reset}", "!", col2=green))
            time.sleep(1)
            self.mainscreen()
            print('\n')
            print('\n')
            print('\n')
            print(Colorate.Color(Colors.green, "[1]Login", True, ))
            print(Colorate.Color(Colors.green, "[2]Register", True, ))
            print(Colorate.Color(Colors.green, "[3]Password Recovery", True, ))
            print(Colorate.Color(Colors.green, "[exit]Quit", True, ))
            inp = input(stage(f"Input : {dark}-> {Col.reset}", "?", col2=bpurple))
            if str(inp) == "1":
                x = self.login()
                if x is True:
                    self.mainscreen()
            elif str(inp) == "2":
                x = self.register()
            elif str(inp) == "3":
                x = self.paswordreset()
            elif inp == "k":
                exit(1)
            elif inp == "g":
                exit(1)
            elif inp == "k":
                exit(1)
            elif inp == "back":
                exit(1)
            elif inp == "exit":
                exit(1)

    def save(self):
        datalist = [
        self.mob,
        self.mobpath,
        self.pocket1,
        self.pocket2,
        self.pocket3,
        self.pocket4,
        self.pocket5,
        self.pocket6,
        self.pocket7,
        self.maxhunt,
        self.atk1,
        self.atk2,
        self.atk3,
        self.atk4,
        self.atk5,
        self.atk6,
        self.atk7,
        self.magelvl
        ]
        pickle.dump(datalist,open("ravensave.dat","wb"))

    def load(self):
        try:
            datalist = pickle.load(open("ravensave.dat","rb"))
        except:
            return
        self.variableswitch(datalist)

    def variableswitch(self,datalist):
        self.mob = datalist[0]
        self.mobpath = datalist[1]
        self.pocket1 = datalist[2]
        self.pocket2 = datalist[3]
        self.pocket3 = datalist[4]
        self.pocket4 = datalist[5]
        self.pocket5 = datalist[6]
        self.pocket6 = datalist[7]
        self.pocket7 = datalist[8]
        self.maxhunt = datalist[9]
        self.atk1 = datalist[10]
        self.atk2 = datalist[11]
        self.atk3 = datalist[12]
        self.atk4 = datalist[13]
        self.atk5 = datalist[14]
        self.atk6 = datalist[15]
        self.atk7 = datalist[16]
        self.magelvl = datalist[17]

    def printer(self,msg):
        print(stagenormal(msg, "!", col2=green))
        return


class MainProcess:
    def __init__(self):
        self.x, self.y, self.w, self.h = None, None, None, None
        self.wincount=0
        self.speed = "Normal"
        self.firstvs = True
        self.xhpbar = None
        self.yhpbar = None
        self.winclosepng = "C:/Users/tolga/Desktop/RavenEnglish-main/img/dwar/mobs/2Level/close.png"
        self.winclose2png = "C:/Users/tolga/Desktop/RavenEnglish-main/img/dwar/mobs/2Level/close2.png"
        self.avlanpng = "C:/Users/tolga/Desktop/RavenEnglish-main/img/dwar/mobs/2Level/avlan.png"
        self.load()

    def start(self):
        errorcounter = 0
        time.sleep(1)
        x, y, w, h = self.findsearch()
        self.x, self.y, self.w, self.h = self.findhunt()
        self.bear = self.waitforimage(bear,5,0.80)
        while True:
            hunt = self.huntmob()
            if hunt is None:
                errorcounter += 1
                self.randomclick(x, y)
                if errorcounter > 20:
                    self.errorcheck()
                    pyautogui.moveTo(self.bedar)
                    pyautogui.click()
                    errorcounter = 0
                    time.sleep(5)
            else:
                time.sleep(1)

    def printer(self,msg):
        print(stagenormal(msg, "!", col2=green))
        return

    def load(self):
        try:
            datalist = pickle.load(open("ravensave.dat","rb"))
        except:
            return
        self.variableswitch(datalist)

    def variableswitch(self,datalist):
        self.mob = datalist[0]
        self.mobpath = datalist[1]
        self.pocket1 = datalist[2]
        self.pocket2 = datalist[3]
        self.pocket3 = datalist[4]
        self.pocket4 = datalist[5]
        self.pocket5 = datalist[6]
        self.pocket6 = datalist[7]
        self.pocket7 = datalist[8]
        self.maxhunt = datalist[9]
        self.atk1 = datalist[10]
        self.atk2 = datalist[11]
        self.atk3 = datalist[12]
        self.atk4 = datalist[13]
        self.atk5 = datalist[14]
        self.atk6 = datalist[15]
        self.atk7 = datalist[16]
        self.magelvl = datalist[17]

    def scr(self,x, y, w, h):
        if x is not None:
            im1 = pyautogui.screenshot(region=(x, y, w, h))
            im1.save(r"./hpbar.png")
            return

    def scrmana(self,x, y, w, h):
        if x is not None:
            im1 = pyautogui.screenshot(region=(x, y, w, h))
            im1.save(r"./manabar.png")
            return

    def aquit(self):
        x = self.checkimage(closebutton, 0.80, None, None, None, None)
        if x is not None:
            pyautogui.moveTo(x)
            pyautogui.click()
            exit("Succes")

    def findhunt(self):
        x = self.waitforimage(test,10,0.85)
        if x is not None:
            first = x
            x = self.waitforimage(test3,10,0.85)
            if x is not None:
                third = x
                w = (third[0] - first[0])
                self.printer("Hunt Window Found!!!")
                v = ("Width", w)
                self.printer(v)
                h = first[1] - third[1]
                v = ("Height", h)
                self.printer(v)
                ############################
                x = first[0]
                y = third[1]
                x += 5
                y += 75
                w -= 24
                h -= 23
                return x, y, w, h

    def randomclick(self,x, y):
        self.errorcheck()
        c = self.checkimage(s1, 0.90, None, None, None, None)
        if c is not None:
            y += 7
            xp = random.randint(0, 128)
            yp = random.randint(0, 44)
            x += xp
            y += yp
            pyautogui.moveTo(x,y)
            pyautogui.click()
            return

    def findsearch(self):
        x = self.waitforimage(s1, 10, 0.90)
        if x is not None:
            first = x
            x = self.waitforimage(s2, 10, 0.90)
            if x is not None:
                third = x
                w = (third[0] - first[0])
                h = first[1] - third[1]
                ############################
                x = first[0]
                y = third[1]
                x += 25
                w -= 18
                h += 1
                # im1 = pyautogui.screenshot(region=(x, y, w, h))
                # im1.save(r"./imsg.png")
                return x, y, w, h
        else:
            self.printer("!HATA:122")
            time.sleep(5)
            exit(122)

    def waitforimage(self,img, tries,conf):
        c = 0
        while c < tries:
            x = self.checkimage(img, conf, None, None, None, None)
            if x is not None:
                self.printer("Görsel Bulundu")
                return x
            else:
                c += 1
                time.sleep(0.2)
        self.printer("Görsel Bekleniyor!!")
        return None

    def waitforimageshort(self,img, tries,conf):
        c = 0
        while c < tries:
            x = self.checkimage(img, conf, None, None, None, None)
            if x is not None:
                self.printer("Görsel Bulundu")
                return x
            else:
                c += 1
        self.printer("Görsel Bekleniyor!!")
        return None

    def errorcheck(self):
        x = self.waitforimage(close,3,0.80)
        if x is not None:
            pyautogui.moveTo(x)
            pyautogui.click()
            time.sleep(0.2)
            pyautogui.moveTo(self.bear)
            pyautogui.click()
            return 1
        x = self.waitforimage(cancel,3,0.80)
        if x is not None:
            pyautogui.moveTo(x)
            pyautogui.click()
            time.sleep(0.2)
            pyautogui.moveTo(self.bear)
            pyautogui.click()
            return 1
        x = self.waitforimage(dead, 1, 0.80)
        if x is not None:
            exit("DEAD")
            #ALARM FUNC HERE

    def errorcheckshort(self):
        x = self.checkimage(close, 0.80, None, None, None, None)
        if x is not None:
            pyautogui.moveTo(x)
            pyautogui.click()
            time.sleep(0.1)
            pyautogui.moveTo(self.bear)
            pyautogui.click()
            return 1
        x = self.checkimage(cancel, 0.80, None, None, None, None)
        if x is not None:
            pyautogui.moveTo(x)
            pyautogui.click()
            time.sleep(0.1)
            pyautogui.moveTo(self.bear)
            pyautogui.click()
            return 1

    def castattack(self,caller):
        if caller == "Up":
            x = self.checkimage(aup, 0.80, None, None, None, None)
            if x is not None:
                pyautogui.moveTo(x)
                pyautogui.click()
                return 1
        elif caller == "Mid":
            x = self.checkimage(amid, 0.80, None, None, None, None)
            if x is not None:
                pyautogui.moveTo(x,)
                pyautogui.click()
                return 1
        elif caller == "Down":
            x = self.checkimage(alow, 0.80, None, None, None, None)
            if x is not None:
                pyautogui.moveTo(x,)
                pyautogui.click()
                return 1
        else:
            return None

    def castmagic(self,caller):
        if caller == "Up":
            pyautogui.click(self.vs)
            pyautogui.press("q")
            return 1
        else:
            return None

    def checkimage(self, image, confidence, x, y, w, h):
        if x == None:
            try:
                img = pyautogui.locateOnScreen(image, grayscale=True, confidence=confidence)
                return img
            except:
                return None
        else:
            try:   
                img = pyautogui.locateOnScreen(image, grayscale=True, confidence=confidence, region=(x, y, w, h))
                return img
            except:
                return None


    def checkwin(self):
        death = self.checkimage("img/global/death.png", 0.80, None, None, None, None)
        if death is not None:
            self.aquit()
        x = self.checkimage(win, 0.80, None, None, None, None)
        if x is not None:
            self.printer("Won!!!")
            rand=random.randint(1,100)
            if rand <70:
                pyautogui.moveTo(self.bear)
                pyautogui.click()
                time.sleep(random.randint(1,2))
                self.wincount += 1
                if self.wincount >= self.maxhunt:
                    self.aquit()
                    self.printer("Kesim Limiti")
                    exit("kesimlimiti")
                return 1
            else:
                winclose = self.checkimage(self.winclosepng,0.80,None,None,None,None)
                if winclose is None:
                        winclose = self.checkimage(self.winclose2png,0.80,None,None,None,None)
                        if winclose is None:
                            pyautogui.moveTo(self.bear)
                            pyautogui.click()
                            time.sleep(random.randint(1,3))
                            self.wincount += 1
                            return 1
                pyautogui.click(winclose)
                time.sleep(random.randint(1,2))
                winclose = self.checkimage(self.avlanpng,0.80,None,None,None,None)
                if winclose is not None:
                    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                pyautogui.moveTo(winclose)
                pyautogui.click()
                self.wincount += 1
                if self.wincount >= self.maxhunt:
                    self.aquit()
                    self.printer("Kesim Limiti")
                    exit("kesimlimiti")
                return 1

    def gamebugfix(self):
        pyautogui.moveTo(self.bear)
        pyautogui.click()
        time.sleep(10)
        x = self.waitforimage(fight, 20, 0.75)
        if x is not None:
            self.fightmodule()
        else:
            return 1

    def mobtemplatematching(self):
        im2 = pyautogui.screenshot('hunt.png')
        img_rgb = cv2.imread('hunt.png')
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread('attacked.png', cv2.IMREAD_GRAYSCALE)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 120)
        cv2.imwrite('res.png',img_rgb)
        global imgg
        imgg=img_rgb
        ######################################
        img_rgb = cv2.imread('res.png')
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(self.mobpath, cv2.IMREAD_GRAYSCALE)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.9
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if "max_loc" in locals():
            return max_loc
        else:
            return None



    def huntmob(self):
        rand=random.randint(1,2)
        time.sleep(rand)
        self.checkwin()
        x = self.mobtemplatematching()
        if x is not None:
            self.printer("Mob Bulundu!!")
            self.printer("Saldiriliyor!!")
            xx=x[0]
            y=x[1]
            pyautogui.moveTo(xx,y)
            if self.mob == ("Disi Ates Orumcegi(3)"):
                pyautogui.move(20, 0)
            elif self.mob == ("Erkek Ates Orumcegi(2)"):
                pyautogui.move(20, 0)
            elif self.mob == ("Erkek Kul Orumcegi(3)"):
                pyautogui.move(20, 0)
            elif self.mob == ("Yasli Cin Kopek(4)"):
                pyautogui.move(20, 0)
                
            pyautogui.move(40, -30)
            pyautogui.click()
            pyautogui.click()
            x = self.errorcheck()
            if x is not None:
                x = random.randint(0,100)
                if x < 50:
                    pyautogui.moveTo(self.bear)
                    pyautogui.click()
                return None
            else:
                x = self.waitforimage(fight, 20, 0.75)
                if x is not None:
                    self.printer("Saldiri Basarili Savas Fonksiyonu Baslatiliyor!!")
                    x = self.fightmodule()
                    if x is not None:
                        return 1
                    else:
                        x = self.gamebugfix()
                        if x == 1:
                            return
                        else:
                            pass
                            # exit("UNKNOWN ERROR")



        else:
            self.printer("Mob Bulunamadı!!")
            return None



    def cokeuse(self):
        #POWER POTİON
        power = self.checkimage(coke, 0.80, None, None, None, None)
        if power is not None:
            x = self.checkimage(minicoke, 0.80, self.xeffect, self.yeffect, 209, 49)
            if x is None:
                pyautogui.moveTo(power)
                pyautogui.click()
                x = random.randint(2,5)
                x = "0"+"."+ str(x)
                x = float(x)
                time.sleep(x)
                self.printer("Power İksiri Kullanıldı")
                return 1
        else:
            return 0

    def manause(self):
        #Mana POTİON
        x = self.checkimage(minimana, 0.80, self.xeffect, self.yeffect, 209, 49)
        if x is None:
            x = self.checkimage(mana, 0.80, None, None, None, None)
            if x is not None:
                if self.pocket1 == "Mana":
                    pyautogui.press("1")
                if self.pocket2 == "Mana":
                    pyautogui.press("2")
                if self.pocket3 == "Mana":
                    pyautogui.press("3")
                if self.pocket4 == "Mana":
                    pyautogui.press("4")
                if self.pocket5 == "Mana":
                    pyautogui.press("5")
                if self.pocket6 == "Mana":
                    pyautogui.press("6")
                if self.pocket7 == "Mana":
                    pyautogui.press("7")
                self.printer("Mana İksiri Kullanıldı")
                time.sleep(1)
                return 1
            else:
                pyautogui.press("tab")
                return 158
        else:
            return 0

    def purpleheal(self):
        #HP POTİON
        hppotion = self.checkimage(milk, 0.80, None, None, None, None)
        if hppotion is not None:
            x = self.checkimage(minimilk, 0.80, self.xeffect, self.yeffect, 209, 49)
            if x is None:
                pyautogui.moveTo(hppotion)
                pyautogui.click()
                self.printer("Heal İksiri Kullanıldı")
                time.sleep(3)
                return 1
        else:
            self.blueheal()

    def blueheal(self):
        #HP POTİON
        hppotion = self.checkimage(blueheal, 0.80, None, None, None, None)
        if hppotion is not None:
            x = self.checkimage(miniblueheal, 0.80, self.xeffect, self.yeffect, 209, 49)
            if x is None:
                pyautogui.moveTo(hppotion)
                pyautogui.click()
                self.printer("Heal İksiri Kullanıldı")
                time.sleep(3)
                return 1
        else:
            self.greenheal()

    def greenheal(self):
        #HP POTİON
        hppotion = self.checkimage(greenheal,0.80, None, None, None, None)
        if hppotion is not None:
            x = self.checkimage(minigreenheal, 0.80, self.xeffect, self.yeffect, 209, 49)
            if x is None:
                pyautogui.moveTo(hppotion)
                pyautogui.click()
                self.printer("Heal İksiri Kullanıldı")
                time.sleep(3)
                return 1
        else:
            self.grayheal()

    def grayheal(self):
        #HP POTİON
        hppotion = self.checkimage(grayheal, 0.80, None, None, None, None)
        if hppotion is not None:
            x = self.checkimage(minigrayheal, 0.80, self.xeffect, self.yeffect, 209, 49)
            if x is None:
                pyautogui.moveTo(hppotion)
                pyautogui.click()
                self.printer("Heal İksiri Kullanıldı")
                time.sleep(3)
                return 1
        else:
            return 0

    def hpcheck(self):
        self.scr(self.xhpbar, self.yhpbar, 7, 11)
        frame = cv2.imread("hpbar.png")
        if True:
            key = "purple"
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            kernel = np.ones((2, 2), np.uint8)

            low = 0, 251, 53
            up = 0, 255, 88

            mask = cv2.inRange(hsv, low, up)
            mask = cv2.erode(mask, kernel, iterations=0)
            mask = cv2.dilate(mask, kernel, iterations=2)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
            ###################################
            if len(cnts) > 0:
                x = self.purpleheal()
            else:
                pass

    def manacheck(self):
        self.scrmana(self.xmanabar, self.ymanabar, 9, 10)
        frame = cv2.imread("manabar.png")
        if True:
            key = "purple"
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            kernel = np.ones((2, 2), np.uint8)

            low = 106, 255, 53
            up = 109, 255, 97

            mask = cv2.inRange(hsv, low, up)
            mask = cv2.erode(mask, kernel, iterations=0)
            mask = cv2.dilate(mask, kernel, iterations=2)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
            ###################################
            if len(cnts) > 0:
                x = self.manause()
                if x == 158:
                    return 158
            else:
                pass

    def firstuse(self):
        if self.pocket1 == "Use At Start":
            pyautogui.press("1")
            time.sleep(1.5)
        if self.pocket2 == "Use At Start":
            pyautogui.press("2")
            time.sleep(1.5)
        if self.pocket3 == "Use At Start":
            pyautogui.press("3")
            time.sleep(1.5)
        if self.pocket4 == "Use At Start":
            pyautogui.press("4")
            time.sleep(1.5)
        if self.pocket5 == "Use At Start":
            pyautogui.press("5")
            time.sleep(1.5)
        if self.pocket6 == "Use At Start":
            pyautogui.press("6")
            time.sleep(1.5)
        if self.pocket7 == "Use At Start":
            pyautogui.press("7")
            time.sleep(1.5)
        return

    def mage(self):
        counter = 1
        errorcount = 0
        while errorcount < 20:
            self.errorcheckshort()
            c = self.checkwin()
            if c is not None:
                return 1
            x = self.waitforimageshort(mage, 5, 0.75)
            if x is not None:
                errorcount = 0
                self.hpcheck()
                x = self.manacheck()
                if x == 158:
                    return 158
                if counter == 1:
                    if self.atk1 != "None":
                        x = self.castmagic("Up")
            else:
                errorcount += 1
        return None

    def fightmodule(self):
        counter = 1
        errorcount = 0
        if self.firstvs is True:
            x = self.waitforimage(fight, 10, 0.75)
            xv, yv, wv, hv = x[0], x[1], x[2], x[3]
            self.xhpbar = int(xv) - 81
            self.yhpbar = int(yv) + 33
            self.xmanabar = int(xv) - 120
            self.ymanabar = int(yv) + 47
            self.firstvs = False
            self.xeffect = int(xv) - 195
            self.yeffect = int(yv) + 60
        self.firstuse()
        if self.magelvl == "Açık":
            x = self.mage()
            if x == None:
                return None
            elif x == 1:
                return 1
            elif x == 158:
                print("Normal Saldırıya Geçildi")
        while errorcount < 20:
            self.errorcheckshort()
            c = self.checkwin()
            if c is not None:
                return 1
            x = self.waitforimageshort(sword, 5, 0.75)
            if x is not None:
                errorcount = 0
                self.hpcheck()
                if counter == 1:
                    self.randomattack()
                    if self.atk1 != "None":
                        self.cokeuse()
                        x = self.castattack(self.atk1)
                        if x is not None:
                            counter += 1
                    else:
                        counter = 1
                elif counter == 2:
                    self.randomattack()
                    if self.atk2 != "None":
                        self.cokeuse()
                        x = self.castattack(self.atk2)
                        if x is not None:
                            counter += 1
                    else:
                        counter = 1
                elif counter == 3:
                    self.randomattack()
                    if self.atk3 != "None":
                        self.cokeuse()
                        x = self.castattack(self.atk3)
                        if x is not None:
                            counter += 1
                    else:
                        counter = 1
                elif counter == 4:
                    self.randomattack()
                    if self.atk4 != "None":
                        self.cokeuse()
                        x = self.castattack(self.atk4)
                        if x is not None:
                            counter += 1
                    else:
                        counter = 1
                elif counter == 5:
                    self.randomattack()
                    if self.atk5 != "None":
                        self.cokeuse()
                        x = self.castattack(self.atk5)
                        if x is not None:
                            counter += 1
                    else:
                        counter = 1
                elif counter == 6:
                    self.randomattack()
                    if self.atk6 != "None":
                        self.cokeuse()
                        x = self.castattack(self.atk6)
                        if x is not None:
                            counter += 1
                    else:
                        counter = 1
                elif counter == 7:
                    self.randomattack()
                    if self.atk7 != "None":
                        self.cokeuse()
                        x = self.castattack(self.atk7)
                        if x is not None:
                            counter += 1
            else:
                errorcount += 1
        return None
     
    def randomattack(self):
        rd =random.randint(1,100)
        if rd <5:
             rd =random.randint(1,3) 
             if rd ==1:
                 self.castattack("Up")
             elif rd ==2:
                 self.castattack("Mid")
             elif rd ==3:
                 self.castattack("Down")
        return
        

if __name__ == '__main__':
    x = Gui()
    x.startmenu()

