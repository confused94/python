# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 21:54:00 2023

@author: ekrem
"""

veri="23546251895"
toplam=0

for x in veri[:10]:
    deger=int(x)
    toplam+=deger
  

strtoplam=str(toplam)


if(len(veri)!=11):
    print("tc kimlik no 11 karakterden oluşmalıdır")


elif(strtoplam[-1]==veri[-1]):
    print("Tc kimlik no geçerli")
    
    
    
else:
  print("tc kimlik no geçerli değil")

    


