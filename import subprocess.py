# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 22:12:30 2023

@author: Ekrem Burak Onuş
"""

import subprocess
secim=input("""Açmak istediğiniz uygulamanın 
kısayolunu giriniz..
Notepad        "N"
Hesap Makinesi "H"
Paint          "P" 
WordPad        "W"
Giriniz:""").upper()

def uygulama():
    if secim=="N":
        subprocess.call("notepad.exe")
    elif secim=="H":
        subprocess.call("calc")
    elif secim=="P":
        subprocess.call("mspaint.exe")
    elif secim=="W":
        subprocess.call("write.exe")
    else:
        print("böyle bir kısayol bulunmamaktadır.")
        
uygulama()        
   
                
                
                


