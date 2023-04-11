# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 21:55:48 2023

@author: ekrem
"""
import random

print("******************Sayı Tahmin Oyunu****************")

s1=int(input("Sayı tahmin ediniz"))
s2=int(input("Sayı tahmin ediniz"))
s3=int(input("Sayı tahmin ediniz"))
s4=int(input("Sayı tahmin ediniz"))
s5=int(input("Sayı tahmin ediniz"))
s6=int(input("Sayı tahmin ediniz"))

bs1=random.randint(1,10)
bs2=random.randint(1,10)
bs3=random.randint(1,10)
bs4=random.randint(1,10)
bs5=random.randint(1,10)
bs6=random.randint(1,10)

print("Tahmin ettiğiniz sayılar:",s1,s2,s3,s4,s5,s6)
print("Bilgisayarın Tahmin ettiği sayılar",bs1,bs2,bs3,bs4,bs5,bs6)

toplamtutar=0
tahminsayisi=0

if(s1==bs1):
    toplamtutar+=10
    tahminsayisi+=1
if(s2==bs2):
    toplamtutar+=10
    tahminsayisi+=1
if(s3==bs3):
    toplamtutar+=10
    tahminsayisi+=1
if(s4==bs4):
    toplamtutar+=10
    tahminsayisi+=1
if(s5==bs5):
    toplamtutar+=10
    tahminsayisi+=1
if(s6==bs6):
   toplamtutar+=10
   tahminsayisi+=1


print("Toplam Bildiğiniz Sayi {} Toplam kazancınız {}".format(tahminsayisi,toplamtutar))
    