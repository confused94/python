# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:02:32 2023

@author: Ekrem Burak Onuş
"""

def nothesaplama(x,y,z):
    
    sonuc=(x+y+z)/3
    return print("Notlarınız\n--------\n{}\t{}\t{}\nOrtalamanız:{}".format(not1,not2,not3,int(sonuc)))



print("********Öğrenci Not Hesaplama***********")
not1=int(input("1. not:"))
not2=int(input("2. not:"))
not3=int(input("3. not:"))

nothesaplama(not1,not2,not3)

