# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 22:57:26 2023

@author: ekrem
"""

# random şifre oluşturma ilk 2 harf son iki rakam 4 karakterli

import random


harf="abcdefghjklmnoprstuvyz"
rakam="123456789"
harfs=""
rakams=""

for x in range(2):
    harfs+=random.choice((harf))
    

for i in range(2):
    rakams+=random.choice(rakam)

  
    
    
print(harfs+rakams)