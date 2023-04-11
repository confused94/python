# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:38:45 2023

@author: ekrem
"""

toplam=0
dongusayı=0

for x in range(1,100,1):
    if(x%7==0):
        toplam=x+toplam
        dongusayı=dongusayı+1


ort=toplam/dongusayı

print("Toplam= {}  Ortalama = {}".format(toplam,ort))        