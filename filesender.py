#-*-coding:utf8;-*-

import socket
import time
from threading import Thread
import sys

port = 1123

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def setmode():
    global mode
    print("Lutfen Mod Secin.\n\tAl\t[0]\n\tGonder\t[1]")
    try:
        mode = int(input(">>"))
        if not mode in [0, 1]:
            print("yanlis bir deger girdiniz.")
            setmode()
         
    except ValueError:
        print("yanlis bir deger girdiniz")
        setmode()

def getservip():
    global ip
    print("lutfen server icin bir ip giriniz\n localip icin 1 e basin")
    ip = input(">>")
    if ip == "1":
        ip = '127.0.0.1'
        print("ip localhost olarak secildi.")
    else:
        print("ip "+ip+" olarak secildi.")   

def getpath():
    global recpath
    print("\nlutfen dosya alinacak klasoru\nolusturup yaziniz.\nornek: /sdcard/path/\n/sdcard/ olarak ayarlamak icin 1 e basin.")
    recpath = input(">>")
    if recpath == "1":
        recpath = "/sdcard/"
    print("dizin "+recpath+" olarak secildi.")
    print("gonderici bekleniyor..")
    
def getfilename():
    global filename
    filename = c.recv(1024).decode("UTF-8")    
    while filename:
        if 'filename' in filename:
            filename = filename.split(" ")
            filename = filename[1]
            filename = ''.join(filename)
            break
            
def makefile():
    global dosya
    dosya = open(recpath+filename, "wb")
    
def readfile():
    global dosya
    global filename
    filename = input("lutfen dosya adini giriniz.\n>>")
    dosya = open(filename, "rb")
    
def connect():
    s.connect((ip, port))
    print("baglanti basarili.")
    
def sendfilename():
    a = filename.split("/")
    a = a[-1]
    a = ''.join(a)
    a = "filename " + a
    s.send(bytes(a, "UTF-8"))
            
    
def writefile():
    global comp
    while 1:
        gelendosya = c.recv(1024)
        dosya.write(gelendosya)
        if not gelendosya:
            break
    dosya.close()
    comp = 1
    print("\nAlma islemi basarili")
    
def bekle():
    input("baslamak icin 1 yazin.")
    
def sendfile():
    global comp
    l = dosya.read(1024)
    while l:
        s.send(l)
        l = dosya.read(1024)
    comp = 1
    print("\nGonderme Islemi Basarili")

def bind():
    global c
    global addr
    s.bind((ip, port))
    s.listen(2)
    c, addr=s.accept()
    
def loading():
    a = 0
    while not comp:
        a = a + 1
        print("gecen sure: ",a," milisaniye")
        time.sleep(0.1)

def main():
    global comp
    comp = 0
    t1 = Thread(target=loading, args=())
    setmode()
    if not mode:
        getservip()
        getpath()
        bind()
        getfilename()
        makefile()
        t1.start()
        writefile()
    elif mode:
        getservip()
        readfile()
        connect()
        sendfilename()
        t1.start()
        sendfile()
if __name__=='__main__':
    main()
        
        
        
        
