# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 22:07:15 2023

@author: Ekrem Burak Onuş
"""
import time
def caykahvematik():
     print("ÇAY-KAHVE MATik")
     time.sleep(2)
     deger=int(input("Çay için 1 e basın\nKahve için 2 ye basın\n"))
     time.sleep(2)
     if deger==1:
         print("Çay seçildi")
         time.sleep(3)
         while True:
             seker=input("Şeker için seceneklerden birini yazın\n AZ ORTA ÇOK\n").upper()
             if seker=="AZ":
                 print(seker,"şeker eklendi")
                 time.sleep(2)
                 break
             elif seker=="ORTA":
                 print(seker,"şeker eklendi")
                 time.sleep(2)
                 break
             elif seker=="ÇOK":
                 print(seker,"şeker eklendi")
                 time.sleep(2)
                 break
             else:
                 print("Yanlış seçim yaptınız")
         print("Çayınız hazırlanıyor lütfen biraz bekleyin")
         time.sleep(4)
         return print("HAZIR")
     elif deger==2:
         while True:
             print("Kahve seçtiniz")
             time.sleep(3)
             seker=input("Şeker için seceneklerden birini yazın\nAZ\nORTA\nÇOK\n").upper()
             if seker=="AZ":
                 print(seker,"şeker eklendi")
                 time.sleep(2)
                 break
             elif seker=="ORTA":
                 print(seker,"şeker eklendi")
                 time.sleep(2)
                 break
             elif seker=="ÇOK":
                 print(seker,"şeker eklendi")
                 time.sleep(2)
                 break
             else:
                 print("Yanlış seçim yaptınız")
         print("Kahveniz hazırlanıyor lütfen biraz bekleyin")
         time.sleep(6)
         print("Hazır\nAfiyet olsun:)")
         
         
        
     
         
caykahvematik()  
     








   
    