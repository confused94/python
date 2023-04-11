# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:43:03 2023

@author: ekrem
"""

vize=int(input("Vize Notunuzu giriniz : "))
final=int(input("final notunuzu giriniz :"))
ort=(vize+final)/2


if(ort>0 and ort<50):
    print("Harf notunuz FF")
elif(ort>=50 and ort<60):
    print("Harf notunuz DD")
elif(ort>=60 and ort<70):
    print("Harf notunuz CC")
elif(ort>=70 and ort<90):
    print("Harf notunuz BB")
elif(ort>=90 and ort<=100):
    print("Harf notunuz AA")
    