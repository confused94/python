# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 19:27:43 2023

@author: Ekrem Burak Onuş
"""



"""kullanıcı şifreyi doğru girerse notepad uygulaması açılacaktır. 3 kere yanlış girme hakkı vardır.3 kere yanlış girerse bekleme süresi başlayacak
ve süre sonunda tekrardan 3 hakkı olacaktır"""

import subprocess
import time
hak=1
güncel_sifre="ekrem94"

while True:
    sifre_giris=input("Şifre: ")
  
    if güncel_sifre==sifre_giris:
        print("Uygulama açılıyor.... Biraz Bekleyin")
        subprocess.call("notepad")
    elif güncel_sifre!=sifre_giris and hak<3:
        print("Yanlış şifre Tekrar deneyin")
        hak+=1
       
    else:
        print("Lütfen süre boyunca bekleyiniz....")
        for i in range(10,0,-1):
            time.sleep(1)
            print(i)
        hak=1    
          
            
        
