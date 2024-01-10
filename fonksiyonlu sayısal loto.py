# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:10:58 2023

@author: Ekrem Burak Onuş
"""

#Sayısal loto programı
import random
import time
def sayısalloto(sayilar):
    tahminler=[]
    sayi=0
    print("Çıkan sayılar\n------\n")
    for i in range(5):
        x=random.randint(1,10)
        tahminler.append(x)
        print(*"-",tahminler[i],sep="",end="\r")
        
        time.sleep(1)
    for j in sayilar:
        if j in tahminler:
              sayi+=1      
            
            
    print("\n")
    return sayi                  


def player():
    sayilar=[]
    for i in range(5):
        x=int(input("Tahminde bulun:"))
        sayilar.append(x)
    tahmin=sayısalloto(sayilar)
    print("Sizin seçtikleriniz\n------\n")
    for j in sayilar:
        print(*"-",j,sep="",end="\r")
        time.sleep(0.3)
    if tahmin==4:
        print("\nküçük ikramiyeyi kazandınız")
    
    elif tahmin==5:
        print("\nBüyük ikramiyeyi kazandınız")
    else:
        print("\nMalesef kazanamadınız")
   
  
player()  
    
        