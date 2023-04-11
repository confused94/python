# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:04:40 2023

@author: ekrem
"""
import random
kart_tuple=("kupa","karo","sinek","maça")
kart_yuz=("1","2","3","4","5","6","7","8","9","10","kız","papaz","joker")

kart=random.choice(kart_tuple)
yuz=random.choice(kart_yuz)


kartınız=kart+yuz

print(kartınız)

#internet adresi

print("http:/falderyası/kartoyunu/rastgelekart/"+kartınız)
