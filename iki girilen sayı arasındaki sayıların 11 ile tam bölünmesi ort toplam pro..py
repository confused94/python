# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 21:02:13 2023

@author: ekrem
"""

s1=int(input("1. sayıyı giriniz"))
s2=int(input("2. sayıyı giriniz"))

dongu=0
toplam=0
for x in range(s1,s2,1):
    dongu=dongu+1
    if(x%11==0):
        toplam=x+toplam
ort=toplam/dongu

print("toplam=",toplam,"Ortalama=",ort)        
 
        
 