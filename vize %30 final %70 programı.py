# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:16:46 2023

@author: ekrem
"""

vize=float(input("Vize notunuzu giriniz :"))
final=float(input("final notunuzu giriniz :"))
vize_30=vize*0.30
final_70=final*0.70
ort=(vize_30+final_70)/2

print("Vize notunuzun %30'u = {}\nFinal notunuzun %70={}\nOrtalamanız={}".format(vize_30,final_70,ort))

