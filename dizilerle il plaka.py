# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:04:26 2023

@author: ekrem
"""

sehir=["adana","bursa","adıyaman","ankara","balıkesir","bingöl","afyon","artvin","burdur","bitlis","aydın","amasya","antalya","bilecik","bolu","agrı"]
sorgu=input(" İsim İle Ara\t 'N' basın.\n Plaka İle Ara\t 'P' basın.\n TUŞ:").upper()
sehir_s=""
plaka_s=0
sehir.sort()

if sorgu=="N":
    sehir_s=input("Sehir İsmi Giriniz:").lower()
    print(sehir.index(sehir_s)+1)
elif sorgu=="P":
    plaka_s=int(input("Plaka No giriniz:"))
    print(sehir[plaka_s-1])
else:
    print("Yanlış tuşlama yaptınız.\a")    
    
    
    
    
