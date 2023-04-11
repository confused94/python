# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:21:14 2023

@author: ekrem
"""

sayilar=[]
toplam=0
ort=0
for i in range(10):
      sayilar.append(int(input("sayi girin:")))
      toplam+=sayilar[i]


ort=toplam/len(sayilar)

sayilar.sort()
print("""Girdiğiniz sayıların toplamı {} iken ortalaması {} şeklindedir.
      Listenizin en büyük değeri {} ve en küçük değeri de {} gibidir."""
      .format(toplam,ort,sayilar[-1],sayilar[0]))