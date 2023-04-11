# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 21:24:10 2023

@author: Ekrem Burak Onuş
"""

sayı1=int(input("Sayı giriniz: "))
sayı2=int(input("Sayı giriniz: "))
islem=input("Yapmak istediğiniz işlemi yazınız(örn +-/*): ")
def hesapmakinesi():
    if islem=="+":
        print("Sonuc =",sayı1+sayı2)
    elif islem=="-":
        print("Sonuc=",sayı1-sayı2)
    elif islem=="*":
        print("sonuc=",sayı1*sayı2)
    elif islem=="/":
        print("sonuc=",sayı1/sayı2)
    else:
        print("yanlış tuşlama yaptınız")
hesapmakinesi()        



    