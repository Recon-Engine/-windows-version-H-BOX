import subprocess

from tkmacosx import Button
from tkinter import *

import os

def tiktok():
    print("This is the output from the script RepT.exe in terminal")
    subprocess.call('.\software\Tiktok\RepT.exe', shell=True)

def ddos():
    print("This is the output from the script DDOS.exe in terminal")
    subprocess.call('.\software\DDOS\DDOS.exe', shell=True)


def spider():
    print("This is the output from the script SpiderMail.exe in terminal")
    subprocess.call('.\software\Spider Mail\SpiderMail.exe', shell=True)

def browser():
    print("This is the output from the script Eternals.exe in terminal")
    subprocess.call('.\software\Browsers\Eternals.exe', shell=True)

def deface():
    print("This is the output from the script deface.exe in terminal")
    subprocess.call('.\software\deface\deface.exe', shell=True)

def Injection():
    print("This is the output from the script SQL Injector.exe in terminal")
    subprocess.call('.\software\Injection\SQL Injector.exe', shell=True)

def callback():
    os.system('python3 NotePad.py')


def WST():
    print("This is the output from the script Web-ST.exe in terminal")
    subprocess.call('.\software\Web-ST\Web-ST.exe', shell=True)

def MSC():
    print("This is the output from the script MSC.exe in terminal")
    subprocess.call('.\software\MSC\MSC.exe', shell=True)

def BPS():
    print("This is the output from the script Bypasser.exe in terminal")
    subprocess.call('.\software\SVB\Bypasser.exe', shell=True)

def DNSx():
    print("This is the output from the script DNS-X.exe in terminal")
    subprocess.call('.\software\DNS-X\DNS-X.exe', shell=True)


def AdminP():
    print("This is the output from the script AD-P.exe in terminal")
    subprocess.call('.\software\Admin-P\AD-P.exe', shell=True)


def SecScan():
    print("This is the output from the script Joomla.exe in terminal")
    subprocess.call('.\software\Sec-Scan\Joomla.exe', shell=True)


def BOLT():
    print("This is the output from the script Bolt-AIO-v1.exe in terminal")
    subprocess.call('.\software\BOLT\Bolt-AIO-v1.exe', shell=True)


def doxrapist():
    print("This is the output from the script DoxRapist.exe in terminal")
    subprocess.call('.\software\DoxRapist-Tool\DoxRapist.exe', shell=True)


def instabot():
    print("This is the output from the script InstagramBot.exe in terminal")
    subprocess.call('.\software\InstaBot\InstagramBot.exe', shell=True)

def QM():
    print("You can login as root for both username and password")
    subprocess.call('.\software\QM\Quarantine.exe', shell=True)

def EMB():
    print("This is the output from the script EMB.exe in terminal")
    subprocess.call('.\software\EMB\EMB.exe', shell=True)

def DORK():
    print("This is the output from the script DORK1.exe in terminal")
    subprocess.call('.\software\MAS-D-S\DORK1.exe', shell=True)

def toolsmenu():
    toolsmenu = Tk()
    toolsmenu.title('TOOLS MENU')
    toolsmenu.config(bg="black", highlightbackground = "#26f7fd", highlightcolor= "#26f7fd", highlightthickness=3)
    toolsmenu.geometry("635x420")

    B3 = Button(toolsmenu, text="DOX-RAPIST TOOL", command=doxrapist)
    B3.config(width=43, height=2, bg="black", foreground="red", activeforeground="red", activebackground="black")
    B3.place(x=3, y=93)

    B3 = Button(toolsmenu, text="INSTAGRAM BOT", command=instabot)
    B3.config(width=43, height=2, bg="black", foreground="red", activeforeground="red", activebackground="black")
    B3.place(x=3, y=183)

    B4 = Button(toolsmenu, text="QUARANTINE : Multitool :", command=QM)
    B4.config(width=43, height=2, bg="black", foreground="red", activeforeground="red", activebackground="black")
    B4.place(x=3, y=3)

    B3 = Button(toolsmenu, text="EMAIL BOMBER", command=EMB)
    B3.config(width=43, height=2, bg="black", foreground="red", activeforeground="red", activebackground="black")
    B3.place(x=3, y=228)

    B4 = Button(toolsmenu, text="CRACKING TOOL", command=BOLT)
    B4.config(width=43, height=2, bg="black", foreground="red", activeforeground="red", activebackground="black")
    B4.place(x=3, y=138)


    B5 = Button(toolsmenu, text="JOOMLA Vuln-Scan", command=SecScan)
    B5.config(width=43, height=2, bg="black", foreground="red", activeforeground="red", activebackground="black")
    B5.place(x=3, y=48)

    B6 = Button(toolsmenu, text="ADMIN PAGE FINDER", command=AdminP)
    B6.config(width=43, height=2, bg="black", foreground="red", activeforeground="red", activebackground="black")
    B6.place(x=316, y=93)

    B7 = Button(toolsmenu, text="DNS EXTRACTOR", command=DNSx)
    B7.config(width=43, height=2, bg="black", foreground="red", activeforeground="red", activebackground="black")
    B7.place(x=316, y=228)

    B8 = Button(toolsmenu, text="SURVEY BYPASSER", command=BPS)
    B8.config(width=43, height=2, bg="black", foreground="red", activeforeground="red", activebackground="black")
    B8.place(x=316, y=183)

    B9 = Button(toolsmenu, text="WEB SOURCE TOOLS", command=WST)
    B9.config(width=43, height=2, bg="black", foreground="red", activeforeground="red", activebackground="black")
    B9.place(x=316, y=138)

    B10 = Button(toolsmenu, text="MULTI SITE CHECKER", command=MSC)
    B10.config(width=43, height=2, bg="black", foreground="red", activeforeground="red", activebackground="black")
    B10.place(x=316, y=48)

    B11 = Button(toolsmenu, text="MASS DORK SCANNER", command=DORK)
    B11.config(width=43, height=2, bg="black", foreground="red", activeforeground="red", activebackground="black")
    B11.place(x=316, y=3)

    B12 = Button(toolsmenu, text="SQL INJECTOR", command=Injection)
    B12.config(width=43, height=2, bg="black", foreground="red", activeforeground="red", activebackground="black")
    B12.place(x=3, y=273)

    B14 = Button(toolsmenu, text="DEFACE CREATOR", command=deface)
    B14.config(width=43, height=2, bg="black", foreground="red", activeforeground="red", activebackground="black")
    B14.place(x=3, y=318)

    B13 = Button(toolsmenu, text="ETERNALS WEB-BROWSER", command=browser)
    B13.config(width=43, height=2, bg="black", foreground="red", activeforeground="red", activebackground="black")
    B13.place(x=316, y=273)

    B15 = Button(toolsmenu, text="SPIDER MAIL", command=spider)
    B15.config(width=43, height=2, bg="black", foreground="red", activeforeground="red", activebackground="black")
    B15.place(x=316, y=318)

    B16 = Button(toolsmenu, text="DDOS TOOL", command=ddos)
    B16.config(width=43, height=2, bg="black", foreground="red", activeforeground="red", activebackground="black")
    B16.place(x=3, y=363)

    B17 = Button(toolsmenu, text="TIKTOK REPORT-BOT", command=tiktok)
    B17.config(width=43, height=2, bg="black", foreground="red", activeforeground="red", activebackground="black")
    B17.place(x=316, y=363)

    toolsmenu.resizable(width=False, height=False)




def helloCallBack():
    print("This is the output from the script clumsy.exe in terminal")
    subprocess.call('.\software\ClumsyLagSwitch\clumsy.exe', shell=True)


root = Tk()
root.title('ʜᴀᴄᴋᴇʀꜱ ʙᴏx')
root.geometry("322x215")
root.config(bg="black", highlightbackground = "#26f7fd", highlightcolor= "#26f7fd", highlightthickness=3)
photo = PhotoImage(file = r"icon.png")
root.iconphoto(False, photo)




B = Button(root, text="LAG SWITCH", command=helloCallBack)
B.config(width=43, height=2, bg="black", foreground="#26f7fd", activeforeground="red", activebackground="black")
B.place(x=3, y=105)

B2 = Button(root, text="NOTEPAD", command=callback)
B2.config(width=43, height=2, bg="black", foreground="#26f7fd", activeforeground="red", activebackground="black")
B2.place(x=3, y=150)

B1 = Button(root, text="TOOLS MENU", command=toolsmenu)
B1.config(width=43, height=2, bg="black", foreground="#26f7fd", activeforeground="red", activebackground="black")
B1.place(x=3, y=60)


lb2 = Label(root, text="[ INSTAGRAM : @recon.engine.official_ ]", bg="black", fg="#2e2e2e", height=1, font=("bold", "7")).place(x=63, y=190)


lb = Label(root, text="𝗛 𝗔 𝗖 𝗞 𝗘 𝗥 𝗦 𝗕𝗢𝗫", bg="black", fg="#26f7fd", height=3, font=("bold")).pack()

root.resizable(width=False, height=False)

root.mainloop()
