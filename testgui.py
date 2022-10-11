from pystyle import *
import pwinput
import time
import pyrebase
from urllib.request import urlopen
import pickle
from variables import *
import pyautogui
import random
import cv2
import numpy as np
import datetime
import os


class Gui:
    def __init__(self):
        self.mob = "Krets(1)"
        self.version="0.0.1"
        self.mobpath = None
        self.pocket1 = None
        self.pocket2 = None
        self.pocket3 = None
        self.pocket4 = None
        self.pocket5 = None
        self.pocket6 = None
        self.pocket7 = None
        self.atk1 = "Boş"
        self.atk2 = "Boş"
        self.atk3 = "Boş"
        self.atk4 = "Boş"
        self.atk5 = "Boş"
        self.atk6 = "Boş"
        self.atk7 = "Boş"
        self.maxhunt = 400
        try:
            self.load()
        except:
            self.printer("Kayıt Dosyası Yuklenirken Hata Oluştu!!!")
            time.sleep(3)

    def pocketstring(self,pocket):
        if pocket == 1:
            if self.pocket1 is not None:
                x1 = "[1]Cep1: " + self.pocket1
                return x1
            else:
                x1 = "[1]Cep1: " + "None"
                return x1
        if pocket == 2:
            if self.pocket2 is not None:
                x1 = "[2]Cep2: " + self.pocket2
                return x1
            else:
                x1 = "[2]Cep2: " + "None"
                return x1
        if pocket == 3:
            if self.pocket3 is not None:
                x1 = "[3]Cep3: " + self.pocket3
                return x1
            else:
                x1 = "[3]Cep3: " + "None"
                return x1
        if pocket == 4:
            if self.pocket4 is not None:
                x1 = "[4]Cep4: " + self.pocket4
                return x1
            else:
                x1 = "[4]Cep4: " + "None"
                return x1
        if pocket == 5:
            if self.pocket5 is not None:
                x1 = "[5]Cep5: " + self.pocket5
                return x1
            else:
                x1 = "[5]Cep5: " + "None"
                return x1
        if pocket == 6:
            if self.pocket6 is not None:
                x1 = "[6]Cep6: " + self.pocket6
                return x1
            else:
                x1 = "[6]Cep6: " + "None"
                return x1
        if pocket == 7:
            if self.pocket7 is not None:
                x1 = "[7]Cep7: " + self.pocket7
                return x1
            else:
                x1 = "[7]Cep7: " + "None"
                return x1

    def attackstring(self, pocket):
        if pocket == 1:
            if self.atk1 is not None:
                x1 = "[1]Atak1: " + self.atk1
                return x1
            else:
                x1 = "[1]Atak1: " + "Boş"
                return x1
        if pocket == 2:
            if self.atk2 is not None:
                x1 = "[2]Atak2: " + self.atk2
                return x1
            else:
                x1 = "[2]Atak2: " + "Boş"
                return x1
        if pocket == 3:
            if self.atk3 is not None:
                x1 = "[3]Atak3: " + self.atk3
                return x1
            else:
                x1 = "[3]Atak3: " + "Boş"
                return x1
        if pocket == 4:
            if self.atk4 is not None:
                x1 = "[4]Atak4: " + self.atk4
                return x1
            else:
                x1 = "[4]Atak4: " + "Boş"
                return x1
        if pocket == 5:
            if self.atk5 is not None:
                x1 = "[5]Atak5: " + self.atk5
                return x1
            else:
                x1 = "[5]Atak5: " + "Boş"
                return x1
        if pocket == 6:
            if self.atk6 is not None:
                x1 = "[6]Atak6: " + self.atk6
                return x1
            else:
                x1 = "[6]Atak6: " + "Boş"
                return x1
        if pocket == 7:
            if self.atk7 is not None:
                x1 = "[7]Atak7: " + self.atk7
                return x1
            else:
                x1 = "[7]Atak7: " + "Boş"
                return x1

    def mainscreen(self):
        self.save()
        print(Colorate.Diagonal(Colors.DynamicMIX((green, purple)), Center.XCenter(text)))
        print('\n')
        #print(stagenormal(f"Sürüm 0.0.1 {Col.reset}", "!", col2=green))
        welcome="Hoşgeldin! "+self.ID
        print(stagenormal(welcome, "!", col2=green))
        timeleft="Kalan Günlerin : "+str(self.time)
        print(stagenormal(timeleft, "!", col2=green))

        print('\n')
        mobguitext = "[1]Mob: "
        col1 = mobguitext + self.mob
        print(Colorate.Horizontal(Colors.green_to_blue, col1, 1))
        print(Colorate.Color(Colors.green, "[2]İksir_Ayarları", True, ))
        print(Colorate.Color(Colors.green, "[3]Avlan_Savaş_Ayarları", True, ))
        print(Colorate.Color(Colors.green, "[b]Başla", True, ))
        print(Colorate.Color(Colors.green, "[k]Çıkış", True, ))
        x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
        if x == "1":
            self.blank()
            self.moblvlselect()
        elif x == "2":
            self.potionsettings()
        elif x == "3":
            self.huntsettings()
        elif x == "k":
            return "break"
        elif x == "g":
            return "break"
        elif x == "k":
            return "break"
        elif x == "back":
            return "break"
        elif x == "exit":
            return "break"
        elif x == "b":
            return "start"

    def huntsettings(self):
        while True:
            self.blank()
            self.save()
            c = "[1]Avlanma_Limiti: " + str(self.maxhunt)
            print(Colorate.Color(Colors.green, c, True, ))
            print(Colorate.Color(Colors.green, "[2]Süper_Vuruş_Ayarı ", True, ))
            print(Colorate.Color(Colors.green, "[g]Geri", True, ))
            x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                print(Colorate.Color(Colors.purple, "Değer Değiştiriliyor", True, ))
                try:
                    x = input(stage(f"Sayı Giriniz : {dark}-> {Col.reset}", "?", col2=bpurple))
                    x = int(x)
                    self.maxhunt = x
                except:
                    print(Colorate.Color(Colors.purple, "Lütfen sadece sayı giriniz!", True, ))
                    time.sleep(2)
            elif x == "2":
                self.superattack()
                return
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
            print(Colorate.Color(Colors.green, "[2]Delikopek(1)", True, ))
            print(Colorate.Color(Colors.green, "[k]Ana Menü", True, ))
            x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.mob = "Krets(1)"
                self.mobpath = "img/dwar/mobs/krets.png"
                return x
            elif x == "2":
                self.mob = "Delikopek(1)"
                self.mobpath = "img/dwar/mobs/delikopek.png"
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
            print(Colorate.Color(Colors.green, "[1]Yasliiskelet(2)", True, ))
            print(Colorate.Color(Colors.green, "[2]Erkekatesorumcek(2)", True, ))
            print(Colorate.Color(Colors.green, "[3]Zigred(2)", True, ))
            print(Colorate.Color(Colors.green, "[k]Ana Menü", True, ))
            x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.mob = "Yasliiskelet(2)"
                self.mobpath = "img/dwar/mobs/yasliiskelet.png"
                return x
            elif x == "2":
                self.mob = "Erkekatesorumcek(2)"
                self.mobpath = "img/dwar/mobs/erkekatesorumcek.png"
                return x
            elif x == "3":
                self.mob = "Zigred(2)"
                self.mobpath = "img/dwar/mobs/zigred.png"
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
            print(Colorate.Color(Colors.green, "[1]Azginkopek(3)", True, ))
            print(Colorate.Color(Colors.green, "[2]Reiskrets(3)", True, ))
            print(Colorate.Color(Colors.green, "[3]Disiatesorumcek(3)", True, ))
            print(Colorate.Color(Colors.green, "[4]Savascizigred(3)", True, ))
            print(Colorate.Color(Colors.green, "[5]Savasciiskelet(3)", True, ))
            print(Colorate.Color(Colors.green, "[6]Erkekkulorumcegi(3)", True, ))
            print(Colorate.Color(Colors.green, "[7]Fitsilya(3)", True, ))
            print(Colorate.Color(Colors.green, "[k]Ana Menü", True, ))
            x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.mob = "Azginkopek(3)"
                self.mobpath = "img/dwar/mobs/azginkopek.png"
                return x
            elif x == "2":
                self.mob = "Reiskrets(3)"
                self.mobpath = "img/dwar/mobs/reiskrets.png"
                return x
            elif x == "3":
                self.mob = "Disiatesorumcek(3)"
                self.mobpath = "img/dwar/mobs/disiatesorumcek.png"
                return x
            elif x == "4":
                self.mob = "Savascizigred(3)"
                self.mobpath = "img/dwar/mobs/savascizigred.png"
                return x
            elif x == "5":
                self.mob = "Savasciiskelet(3)"
                self.mobpath = "img/dwar/mobs/savasci.png"
                return x
            elif x == "6":
                self.mob = "Erkekkulorumcegi(3)"
                self.mobpath = "img/dwar/mobs/erkekkulorumcegi.png"
                return x
            elif x == "7":
                self.mob = "Fitsilya(3)"
                self.mobpath = "img/dwar/mobs/fitsilya.png"
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
            print(Colorate.Color(Colors.green, "[1]Yaslicinkopek(4)", True, ))
            print(Colorate.Color(Colors.green, "[2]Erguvanizigred(4)", True, ))
            print(Colorate.Color(Colors.green, "[3]Kocamanzigred(4)", True, ))
            print(Colorate.Color(Colors.green, "[4]Zombi(4)", True, ))
            print(Colorate.Color(Colors.green, "[5]Boz Hakurt(4)", True, ))
            print(Colorate.Color(Colors.green, "[6]Genç Oduni(4)", True, ))
            print(Colorate.Color(Colors.green, "[7]Genç Beron Kaplanı(4)", True, ))
            print(Colorate.Color(Colors.green, "[8]Maharetli Fitsilya(4)", True, ))
            print(Colorate.Color(Colors.green, "[9]Oduni(4)", True, ))
            print(Colorate.Color(Colors.green, "[10]Tecrübeli Beron Kaplanı(4)", True, ))
            print(Colorate.Color(Colors.green, "[11]Buz Hakurtu(4)", True, ))
            print(Colorate.Color(Colors.green, "[12]Krogan(4)", True, ))
            print(Colorate.Color(Colors.green, "[k]Ana Menü", True, ))
            x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.mob = "Yaslicinkopek(4)"
                self.mobpath = "img/dwar/mobs/yaslicinkopek.png"
                return x
            elif x == "2":
                self.mob = "Erguvanizigred(4)"
                self.mobpath = "img/dwar/mobs/erguvanizigred.png"
                return x
            elif x == "3":
                self.mob = "Kocamanzigred(4)"
                self.mobpath = "img/dwar/mobs/kocamanzigred.png"
                return x
            elif x == "4":
                self.mob = "Zombi(4)"
                self.mobpath = "img/dwar/mobs/zombi.png"
                return x
            elif x == "5":
                self.mob = "Boz Hakurt(4)"
                self.mobpath = "img/dwar/mobs/hakurt.png"
                return x
            elif x == "6":
                self.mob = "Genç Oduni(4)"
                self.mobpath = "img/dwar/mobs/gencoduni.png"
                return x
            elif x == "7":
                self.mob = "Genç Beron Kaplanı(4)"
                self.mobpath = "img/dwar/mobs/gencberon.png"
                return x
            elif x == "8":
                self.mob = "Maharetli Fitsilya(4)"
                self.mobpath = "img/dwar/mobs/maharetlifitsilya.png"
                return x
            elif x == "9":
                self.mob = "Oduni(4)"
                self.mobpath = "img/dwar/mobs/oduni.png"
                return True
            elif x == "10":
                self.mob = "Tecrübeli Beron Kaplanı(4)"
                self.mobpath = "img/dwar/mobs/tecrubeliberon.png"
                return True
            elif x == "11":
                self.mob = "Buz Hakurtu(4)"
                self.mobpath = "img/dwar/mobs/buzhakurtu.png"
                return True
            elif x == "12":
                self.mob = "Krogan(4)"
                self.mobpath = "img/dwar/mobs/krogan.png"
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
            print(Colorate.Color(Colors.green, "[1]Durgharg(5)", True, ))
            print(Colorate.Color(Colors.green, "[2]Phadd Ayısı(5)", True, ))
            print(Colorate.Color(Colors.green, "[3]Orman İguaronu(5)", True, ))
            print(Colorate.Color(Colors.green, "[4]Yalnız Gungl(5)", True, ))
            print(Colorate.Color(Colors.green, "[5]Kan Emici Zigred(5)", True, ))
            print(Colorate.Color(Colors.green, "[6]Hortlak(5)", True, ))
            print(Colorate.Color(Colors.green, "[7]Ölü(5)", True, ))
            print(Colorate.Color(Colors.green, "[8]Cin Köpek İskeleti(5)", True, ))
            print(Colorate.Color(Colors.green, "[9]Fetihçi Ork İskeleti(5)", True, ))
            print(Colorate.Color(Colors.green, "[10]Taş Lotusu Sürgünü(5)", True, ))
            print(Colorate.Color(Colors.green, "[11]Kırmızı Baltalar Sürgünü(5)", True, ))
            print(Colorate.Color(Colors.green, "[k]Ana Menü", True, ))
            x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.mob = "Durgharg(5)"
                self.mobpath = "img/dwar/mobs/durgharg.png"
                return True
            elif x == "2":
                self.mob = "Phadd Ayısı(5)"
                self.mobpath = "img/dwar/mobs/phadayi.png"
                return True
            elif x == "3":
                self.mob = "Orman İguaronu(5)"
                self.mobpath = "img/dwar/mobs/ormanigo.png"
                return True
            elif x == "4":
                self.mob = "Yalnız Gungl(5)"
                self.mobpath = "img/dwar/mobs/ygungl.png"
                return True
            elif x == "5":
                self.mob = "Kan Emici Zigred(5)"
                self.mobpath = "img/dwar/mobs/kanemicizigred.png"
                return True
            elif x == "6":
                self.mob = "Hortlak(5)"
                self.mobpath = "img/dwar/mobs/hortlak.png"
                return True
            elif x == "7":
                self.mob = "Ölü(5)"
                self.mobpath = "img/dwar/mobs/olu.png"
                return True
            elif x == "8":
                self.mob = "Cin Köpek İskeleti(5)"
                self.mobpath = "img/dwar/mobs/ckopekiskelet.png"
                return True
            elif x == "9":
                self.mob = "Fetihçi Ork İskeleti(5)"
                self.mobpath = "img/dwar/mobs/fork.png"
                return True
            elif x == "10":
                self.mob = "Taş Lotusu Sürgünü(5)"
                self.mobpath = "img/dwar/mobs/tsurgun.png"
                return True
            elif x == "11":
                self.mob = "Kırmızı Baltalar Sürgünü(5)"
                self.mobpath = "img/dwar/mobs/ksurgun.png"
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
            print(Colorate.Color(Colors.green, "[1]Tecrübeli Durgharg(6)", True, ))
            print(Colorate.Color(Colors.green, "[2]Kodrag(6)", True, ))
            print(Colorate.Color(Colors.green, "[3]Yaşlı Phadd Ayısı(6)", True, ))
            print(Colorate.Color(Colors.green, "[4]Gordt(6)", True, ))
            print(Colorate.Color(Colors.green, "[5]Toprak Golemi(6)", True, ))
            print(Colorate.Color(Colors.green, "[6]GungIDO(6)", True, ))
            print(Colorate.Color(Colors.green, "[7]Rukkub İskeleti(6)", True, ))
            print(Colorate.Color(Colors.green, "[8]Taş Lotusu Haini(6)", True, ))
            print(Colorate.Color(Colors.green, "[9]Levremar Askeri(6)", True, ))
            print(Colorate.Color(Colors.green, "[k]Ana Menü", True, ))
            x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.mob = "Tecrübeli Durgharg(6)"
                self.mobpath = "img/dwar/mobs/tdurgharg.png"
                return True
            elif x == "2":
                self.mob = "Kodrag(6)"
                self.mobpath = "img/dwar/mobs/kodrag.png"
                return True
            elif x == "3":
                self.mob = "Yaşlı Phadd Ayısı(6)"
                self.mobpath = "img/dwar/mobs/yphadd.png"
                return True
            elif x == "4":
                self.mob = "Gordt(6)"
                self.mobpath = "img/dwar/mobs/gordt.png"
                return True
            elif x == "5":
                self.mob = "Toprak Golemi(6)"
                self.mobpath = "img/dwar/mobs/tgolem.png"
                return True
            elif x == "6":
                self.mob = "GungIDO(6)"
                self.mobpath = "img/dwar/mobs/gungdo.png"
                return True
            elif x == "7":
                self.mob = "Rukkub İskeleti(6)"
                self.mobpath = "img/dwar/mobs/rukkub.png"
                return True
            elif x == "8":
                self.mob = "Taş Lotusu Haini(6)"
                self.mobpath = "img/dwar/mobs/taslotusuhaini.png"
                return True
            elif x == "9":
                self.mob = "Levremar Askeri(6)"
                self.mobpath = "img/dwar/mobs/levremarasker.png"
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
            print(Colorate.Color(Colors.green, "[1]Levremar Lejyoneri(7)", True, ))
            print(Colorate.Color(Colors.green, "[2]Genç Valdagor Kurdu(7)", True, ))
            print(Colorate.Color(Colors.green, "[3]Valdagor Kurdu(7)", True, ))
            print(Colorate.Color(Colors.green, "[4]Eşkiya Gordt(7)", True, ))
            print(Colorate.Color(Colors.green, "[5]Taş Golem(7)", True, ))
            print(Colorate.Color(Colors.green, "[6]Sivri Dişli Kaplan(7)", True, ))
            print(Colorate.Color(Colors.green, "[7]Sivri Dişli Aksak Kaplan(7)", True, ))
            print(Colorate.Color(Colors.green, "[8]GungIVO(7)", True, ))
            print(Colorate.Color(Colors.green, "[k]Ana Menü", True, ))
            x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.mob = "Levremar Lejyoneri(7)"
                self.mobpath = "img/dwar/mobs/levremarleg.png"
                return True
            elif x == "2":
                self.mob = "Genç Valdagor Kurdu(7)"
                self.mobpath = "img/dwar/mobs/gencvaldagor2.png"
                return True
            elif x == "3":
                self.mob = "Valdagor Kurdu(7)"
                self.mobpath = "img/dwar/mobs/valdagorkurdu.png"
                return True
            elif x == "4":
                self.mob = "Eşkiya Gordt(7)"
                self.mobpath = "img/dwar/mobs/egordt.png"
                return True
            elif x == "5":
                self.mob = "Taş Golem(7)"
                self.mobpath = "img/dwar/mobs/tasgolem.png"
                return True
            elif x == "6":
                self.mob = "Sivri Dişli Kaplan(7)"
                self.mobpath = "img/dwar/mobs/sivridislikaplan.png"
                return True
            elif x == "7":
                self.mob = "Taş Golem(7)"
                self.mobpath = "img/dwar/mobs/sivridisliaksakkaplan.png"
                return True
            elif x == "8":
                self.mob = "GungIVO(7)"
                self.mobpath = "img/dwar/mobs/gungivo.png"
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
            print(Colorate.Color(Colors.green, "[1]Boğazkeser Gordt(8)", True, ))
            print(Colorate.Color(Colors.green, "[2]Gorgulya(8)", True, ))
            print(Colorate.Color(Colors.green, "[3]Beyaz Ayı(8)", True, ))
            print(Colorate.Color(Colors.green, "[4]Eşkiya Yeti Hantu(8)", True, ))
            print(Colorate.Color(Colors.green, "[5]Keşifçi Yeti Yukari(8)", True, ))
            print(Colorate.Color(Colors.green, "[6]Granit Golemi(8)", True, ))
            print(Colorate.Color(Colors.green, "[7]GungHO(8)", True, ))
            print(Colorate.Color(Colors.green, "[k]Ana Menü", True, ))
            x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.mob = "Boğazkeser Gordt(8)"
                self.mobpath = "img/dwar/mobs/bgordt.png"
                return True
            elif x == "2":
                self.mob = "Gorgulya(8)"
                self.mobpath = "img/dwar/mobs/gorgulya2.png"
                return True
            elif x == "3":
                self.mob = "Beyaz Ayı(8)"
                self.mobpath = "img/dwar/mobs/beyazayi.png"
                return True
            elif x == "4":
                self.mob = "Eşkiya Yeti Hantu(8)"
                self.mobpath = "img/dwar/mobs/yetihantu.png"
                return True
            elif x == "5":
                self.mob = "Keşifçi Yeti Yukari(8)"
                self.mobpath = "img/dwar/mobs/yetiyukari.png"
                return True
            elif x == "6":
                self.mob = "Granit Golemi(8)"
                self.mobpath = "img/dwar/mobs/granitgolem.png"
                return True
            elif x == "7":
                self.mob = "GungHO(8)"
                self.mobpath = "img/dwar/mobs/gungho.png"
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
            print(Colorate.Color(Colors.green, "[1]Yırtıcı Gorgulya(9)", True, ))
            print(Colorate.Color(Colors.green, "[2]Avcı Yeti Hantu(9)", True, ))
            print(Colorate.Color(Colors.green, "[3]Zararcı Yeti Yukari(9)", True, ))
            print(Colorate.Color(Colors.green, "[4]Vahşi Buz Ayısı(9)", True, ))
            print(Colorate.Color(Colors.green, "[5]Gardiyan GungHO(9)", True, ))
            print(Colorate.Color(Colors.green, "[k]Ana Menü", True, ))
            x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.mob = "Yırtıcı Gorgulya(9)"
                self.mobpath = "img/dwar/mobs/ygorgulya.png"
                return True
            elif x == "2":
                self.mob = "Avcı Yeti Hantu(9)"
                self.mobpath = "img/dwar/mobs/avcihantu.png"
                return True
            elif x == "3":
                self.mob = "Zararcı Yeti Yukari(9)"
                self.mobpath = "img/dwar/mobs/zararciyukari.png"
                return True
            elif x == "4":
                self.mob = "Vahşi Buz Ayısı(9)"
                self.mobpath = "img/dwar/mobs/vahsibuzayisi.png"
                return True
            elif x == "5":
                self.mob = "Gardiyan GungHO(9)"
                self.mobpath = "img/dwar/mobs/gardiyangungho.png"
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

    def moblvlselect(self):
        while True:
            self.blank()
            print(Colorate.Color(Colors.green, "[1]Seviye 1 Moblar", True, ))
            print(Colorate.Color(Colors.green, "[2]Seviye 2 Moblar", True, ))
            print(Colorate.Color(Colors.green, "[3]Seviye 3 Moblar", True, ))
            print(Colorate.Color(Colors.green, "[4]Seviye 4 Moblar", True, ))
            print(Colorate.Color(Colors.green, "[5]Seviye 5 Moblar", True, ))
            print(Colorate.Color(Colors.green, "[6]Seviye 6 Moblar", True, ))
            print(Colorate.Color(Colors.green, "[7]Seviye 7 Moblar", True, ))
            print(Colorate.Color(Colors.green, "[8]Seviye 8 Moblar", True, ))
            print(Colorate.Color(Colors.green, "[9]Seviye 9 Moblar", True, ))
            print(Colorate.Color(Colors.green, "[k]Ana Menü", True, ))
            x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
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
            print(Colorate.Color(Colors.green, "[g]Geri", True, ))
            x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_red, "[1]Güç", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Hayat", 1))
                x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.pocket1 = "Güç"
                elif x == "2":
                    self.pocket1 = "Hayat"
            elif x == "2":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_red, "[1]Güç", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Hayat", 1))
                x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.pocket2 = "Güç"
                elif x == "2":
                    self.pocket2 = "Hayat"
            elif x == "3":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_red, "[1]Güç", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Hayat", 1))
                x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.pocket3 = "Güç"
                elif x == "2":
                    self.pocket3 = "Hayat"
            elif x == "4":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_red, "[1]Güç", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Hayat", 1))
                x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.pocket4 = "Güç"
                elif x == "2":
                    self.pocket4 = "Hayat"
            elif x == "5":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_red, "[1]Güç", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Hayat", 1))
                x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.pocket5 = "Güç"
                elif x == "2":
                    self.pocket5 = "Hayat"
            elif x == "6":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_red, "[1]Güç", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Hayat", 1))
                x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.pocket6 = "Güç"
                elif x == "2":
                    self.pocket6 = "Hayat"
            elif x == "7":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_red, "[1]Güç", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Hayat", 1))
                x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.pocket7 = "Güç"
                elif x == "2":
                    self.pocket7 = "Hayat"
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
            print(Colorate.Color(Colors.green, "[g]Geri", True, ))
            x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
            x = str(x)
            if x == "1":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_yellow, "[1]Yukarı", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Orta", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[3]Alt", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[4]Boş", 1))
                x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.atk1 = "Yukarı"
                elif x == "2":
                    self.atk1 = "Orta"
                elif x == "3":
                    self.atk1 = "Alt"
                elif x == "4":
                    self.atk1 = "Boş"
            elif x == "2":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_yellow, "[1]Yukarı", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Orta", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[3]Alt", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[4]Boş", 1))
                x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.atk2 = "Yukarı"
                elif x == "2":
                    self.atk2 = "Orta"
                elif x == "3":
                    self.atk2 = "Alt"
                elif x == "4":
                    self.atk2 = "Boş"
            elif x == "3":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_yellow, "[1]Yukarı", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Orta", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[3]Alt", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[4]Boş", 1))
                x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.atk3 = "Yukarı"
                elif x == "2":
                    self.atk3 = "Orta"
                elif x == "3":
                    self.atk3 = "Alt"
                elif x == "4":
                    self.atk3 = "Boş"
            elif x == "4":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_yellow, "[1]Yukarı", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Orta", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[3]Alt", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[4]Boş", 1))
                x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.atk4 = "Yukarı"
                elif x == "2":
                    self.atk4 = "Orta"
                elif x == "3":
                    self.atk4 = "Alt"
                elif x == "4":
                    self.atk4 = "Boş"
            elif x == "5":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_yellow, "[1]Yukarı", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Orta", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[3]Alt", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[4]Boş", 1))
                x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.atk5 = "Yukarı"
                elif x == "2":
                    self.atk5 = "Orta"
                elif x == "3":
                    self.atk5 = "Alt"
                elif x == "4":
                    self.atk5 = "Boş"
            elif x == "6":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_yellow, "[1]Yukarı", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Orta", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[3]Alt", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[4]Boş", 1))
                x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.atk6 = "Yukarı"
                elif x == "2":
                    self.atk6 = "Orta"
                elif x == "3":
                    self.atk6 = "Alt"
                elif x == "4":
                    self.atk6 = "Boş"
            elif x == "7":
                self.blank()
                print(Colorate.Horizontal(Colors.green_to_yellow, "[1]Yukarı", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[2]Orta", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[3]Alt", 1))
                print(Colorate.Horizontal(Colors.green_to_yellow, "[4]Boş", 1))
                x = input(stage(f"Girdi : {dark}-> {Col.reset}", "?", col2=bpurple))
                x = str(x)
                if x == "1":
                    self.atk7 = "Yukarı"
                elif x == "2":
                    self.atk7 = "Orta"
                elif x == "3":
                    self.atk7 = "Alt"
                elif x == "4":
                    self.atk7 = "Boş"
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
        except:
            usernameaddgmail = self.Usernamea + "@gmail.com"
            try:
                self.userlog = auth.sign_in_with_email_and_password(usernameaddgmail, self.Passworda)
            except:
                usernameaddhotmail = self.Usernamea + "@hotmail.com"
                try:
                    self.userlog = auth.sign_in_with_email_and_password(usernameaddhotmail, self.Passworda)
                except:
                    print(stagenormal(f"Kullanıcı adı veya şifre geçersiz {Col.reset}", "!", col2=red))
                    print(stagenormal(f"3 saniye sonra tekrar deneyin {Col.reset}", "!", col2=red))
                    time.sleep(3)
                    return 0
        return 1

    def checktimeleft(self):
        try:
            res = urlopen('http://just-the-time.appspot.com/')
            result = res.read().strip()
            result_str = result.decode('utf-8')
            current = (result_str)
            user = db.child("users").child(self.ID).get(self.userlog['idToken'])
            x = (user.val())
            if x is None:
                exit(31)
            fdata = x["time"]
            x = self.timecalculator(current, fdata)
            if x is None:
                print(stagenormal(f"Üyelik Süresi Tükenmiş Veya Mecvut Değil! {Col.reset}", "!", col2=green))
                time.sleep(3)
                return 0
            else:
                print(stagenormal(f"Giriş Yapıldı! {Col.reset}", "!", col2=green))
                self.time = x
                time.sleep(2)
                return 1
        except:
            print(stagenormal(f"Üyelik Süresi Tükenmiş Veya Mecvut Değil! {Col.reset}", "!", col2=green))
            print(stagenormal(f"Kullanıcı Adınızı Kontrol Ediniz! {Col.reset}", "!", col2=green))
            time.sleep(3)
            return 0

    def checkversion(self):
        versionn = db.child("Version").get(self.userlog['idToken'])
        versionn = (versionn.val())
        version=str(versionn["version"])
        if version !=self.version:
            print(stagenormal(f"Geçersiz Uygulama Sürümü Güncelleyiniz!! {Col.reset}", "!", col2=green))
            time.sleep(3)
            return 0

    def login(self):
        System.Size(75, 22)
        System.Title("Raven Dwar 0.0.1")
        Cursor.HideCursor()
        print(Colorate.Diagonal(Colors.DynamicMIX((green, purple)), Center.XCenter(text)))
        print('\n')
        self.Usernamea = input(stage(f"Kullanıcı Adı : {dark}-> {Col.reset}", "?", col2=bpurple))
        #self.Usernamea = "mrblazer31"
        #self.Passworda = "123123"
        self.ID = self.Usernamea
        self.Passworda = input(stage(f"Şifre : {dark}-> {Col.reset}", "?", col2=bpurple))
        print(stagenormal(f"Giriş Yapılıyor {Col.reset}", "!", col2=dark))
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
        while True:
            self.blank()
            x = self.mainscreen()
            if x == "break":
                exit()
            elif x == "start":
                return "ytzw"

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
        self.atk7
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

    def printer(self,msg):
        print(stagenormal(msg, "!", col2=green))
        return


class MainProcess:
    def __init__(self):
        self.x, self.y, self.w, self.h = None, None, None, None
        self.wincount=0
        self.firstvs = True
        self.xhpbar = None
        self.yhpbar = None
        self.load()

    def start(self):
        errorcounter = 0
        time.sleep(1)
        x, y, w, h = self.findsearch()
        self.x, self.y, self.w, self.h = self.findhunt()
        while True:
            hunt = self.huntmob()
            if hunt is None:
                errorcounter += 1
                self.randomclick(x, y)
                if errorcounter > 20:
                    pyautogui.click(937, 108)
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

    def scr(self,x, y, w, h):
        if x is not None:
            im1 = pyautogui.screenshot(region=(x, y, w, h))
            im1.save(r"./hpbar.png")
            return

    def aquit(self):
        x = pyautogui.locateOnScreen(closebutton, grayscale=True, confidence=0.80)
        if x is not None:
            pyautogui.click(x)
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
        c = pyautogui.locateOnScreen(s1, grayscale=True, confidence=0.90)
        if c is not None:
            y += 7
            xp = random.randint(0, 128)
            yp = random.randint(0, 44)
            x += xp
            y += yp
            pyautogui.click(x, y)
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
                h += 8
                # im1 = pyautogui.screenshot(region=(x, y, w, h))
                # im1.save(r"./imsg.png")
                return x, y, w, h

    def waitforimage(self,img, tries,conf):
        c = 0
        while c < tries:
            x = pyautogui.locateOnScreen(img, grayscale=True, confidence=conf)
            if x is not None:
                self.printer("Görsel Bulundu")
                return x
            else:
                c += 1
                time.sleep(0.2)
        self.printer("Görsel Bekleniyor!!")
        return None

    def errorcheck(self):
        x = pyautogui.locateOnScreen(close, grayscale=True, confidence=0.80)
        if x is not None:
            pyautogui.click(x)
            return 1
        x = pyautogui.locateOnScreen(cancel, grayscale=True, confidence=0.80)
        if x is not None:
            pyautogui.click(x)
            return 1

    def castattack(self,caller):
        if caller == "Yukarı":
            x = pyautogui.locateOnScreen(sword, grayscale=True, confidence=0.80)
            if x is not None:
                pyautogui.click(x)
                pyautogui.press("q")
                return 1
        elif caller == "Orta":
            x = pyautogui.locateOnScreen(sword, grayscale=True, confidence=0.80)
            if x is not None:
                pyautogui.click(x)
                pyautogui.press("w")
                return 1
        elif caller == "Alt":
            x = pyautogui.locateOnScreen(sword, grayscale=True, confidence=0.80)
            if x is not None:
                pyautogui.click(x)
                pyautogui.press("e")
                return 1
        else:
            return None

    def checkwin(self):
        x = pyautogui.locateOnScreen(win, grayscale=True, confidence=0.80)
        if x is not None:
            self.printer("Won!!!")
            x = 1
            if x is not None:
                pyautogui.click(937, 108)
                self.wincount += 1
                if self.wincount == self.maxhunt:
                    self.aquit()
                    self.printer("Kesim Limiti")
                    exit("400 limit")
                return 1

    def gamebugfix(self):
        x = pyautogui.locateOnScreen(bear, grayscale=True, confidence=0.80)
        if x is not None:
            pyautogui.click(x)
            time.sleep(10)
            x = self.waitforimage(fight, 20, 0.75)
            if x is not None:
                self.fightmodule()
            else:
                return 1

    def huntmob(self):
        self.checkwin()
        if self.mob == "Gorgulya(8)":
            x = pyautogui.locateOnScreen(self.mobpath, grayscale=True, confidence=0.90,
                                         region=(self.x, self.y, self.w, self.h))
        else:
            x = pyautogui.locateOnScreen(self.mobpath, grayscale=True, confidence=0.85,
                                         region=(self.x, self.y, self.w, self.h))
        if x is not None:
            self.printer("Mob Bulundu!!")
            self.printer("Tıklamayı Deniyorum!!")
            pyautogui.moveTo(x)
            pyautogui.move(0, -30)
            pyautogui.click()
            pyautogui.click()
            x = self.errorcheck()
            if x is not None:
                return None
            else:
                x = self.waitforimage(fight, 10, 0.75)
                if x is not None:
                    self.printer("Tıklama Başarılı Savaş Fonksiyonu Çağırılıyor!!")
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
        x = pyautogui.locateOnScreen(coke, grayscale=True, confidence=0.80)
        if x is not None:
            x = pyautogui.locateOnScreen(minicoke, grayscale=True, confidence=0.80, region=(self.xeffect, self.yeffect, 209, 49))
            if x is None:
                if self.pocket1 == "Güç":
                    pyautogui.press("1")
                if self.pocket2 == "Güç":
                    pyautogui.press("2")
                if self.pocket3 == "Güç":
                    pyautogui.press("3")
                if self.pocket4 == "Güç":
                    pyautogui.press("4")
                if self.pocket5 == "Güç":
                    pyautogui.press("5")
                if self.pocket6 == "Güç":
                    pyautogui.press("6")
                if self.pocket7 == "Güç":
                    pyautogui.press("7")
                return 1
        else:
            return 0

    def milkuse(self):
        #HP POTİON
        x = pyautogui.locateOnScreen(milk, grayscale=True, confidence=0.80)
        if x is not None:
            x = pyautogui.locateOnScreen(minimilk, grayscale=True, confidence=0.80, region=(self.xeffect, self.yeffect, 209, 49))
            if x is None:
                if self.pocket1 == "Hayat":
                    pyautogui.press("1")
                if self.pocket2 == "Hayat":
                    pyautogui.press("2")
                if self.pocket3 == "Hayat":
                    pyautogui.press("3")
                if self.pocket4 == "Hayat":
                    pyautogui.press("4")
                if self.pocket5 == "Hayat":
                    pyautogui.press("5")
                if self.pocket6 == "Hayat":
                    pyautogui.press("6")
                if self.pocket7 == "Hayat":
                    pyautogui.press("7")
                self.printer("Hayat İksiri Kullanıldı")
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
                x = self.milkuse()
            else:
                pass

    def fightmodule(self):
        counter = 1
        errorcount = 0
        if self.firstvs is True:
            x = self.waitforimage(fight, 10, 0.75)
            xv, yv, wv, hv = x[0], x[1], x[2], x[3]
            self.xhpbar = int(xv) - 81
            self.yhpbar = int(yv) + 33
            self.firstvs = False
            self.xeffect = int(xv) - 195
            self.yeffect = int(xv) + 60
        while errorcount < 20:
            self.errorcheck()
            c = self.checkwin()
            if c is not None:
                return 1
            x = self.waitforimage(sword, 3, 0.75)
            if x is not None:
                errorcount = 0
                self.hpcheck()
                if counter == 1:
                    if self.atk1 != "Boş":
                        self.cokeuse()
                        x = self.castattack(self.atk1)
                        if x is not None:
                            counter += 1
                    else:
                        counter = 1
                elif counter == 2:
                    if self.atk2 != "Boş":
                        self.cokeuse()
                        x = self.castattack(self.atk2)
                        if x is not None:
                            counter += 1
                    else:
                        counter = 1
                elif counter == 3:
                    if self.atk3 != "Boş":
                        self.cokeuse()
                        x = self.castattack(self.atk3)
                        if x is not None:
                            counter += 1
                    else:
                        counter = 1
                elif counter == 4:
                    if self.atk4 != "Boş":
                        self.cokeuse()
                        x = self.castattack(self.atk4)
                        if x is not None:
                            counter += 1
                    else:
                        counter = 1
                elif counter == 5:
                    if self.atk5 != "Boş":
                        self.cokeuse()
                        x = self.castattack(self.atk5)
                        if x is not None:
                            counter += 1
                    else:
                        counter = 1
                elif counter == 6:
                    if self.atk6 != "Boş":
                        self.cokeuse()
                        x = self.castattack(self.atk6)
                        if x is not None:
                            counter += 1
                    else:
                        counter = 1
                elif counter == 7:
                    if self.atk7 != "Boş":
                        self.cokeuse()
                        x = self.castattack(self.atk7)
                        if x is not None:
                            counter += 1
            else:
                errorcount += 1
        return None







if __name__ == '__main__':
    while True:
        x=Gui()
        c = x.login()
        if c == "ytzw":
            x=MainProcess()
            x.start()
