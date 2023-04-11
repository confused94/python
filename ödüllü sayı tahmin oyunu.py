# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 22:18:17 2023

@author: ekrem
"""

print("***********ödüllü-haklı sayı tahmin oyunu*********")

print("ilk sayıyı tahmin eden PARA ÖDülü \n2.Sayıyı Bilen Akülü Oyuncak Araba \n3. Sayıyı bilen Anahtarlık \n4.Sayıyı bilen Kalem Kazanacaktır")

import random
x=1
while x<5:
    bs=random.randint(1,5)
    tahmin=int(input("Sayıyı Tahmin Ediniz :"))
    
    
    if(bs==tahmin):
         if(x==1):
             print("Tebrikler {} denemede bildiniz. 500Tl kazandınız".format(x))
             
         elif(x==2):
             print("Tebrikler {} denemede bildiniz. Akülü ARaba kazandınız".format(x))
         elif(x==3):
             print("Tebrikler {} denemede bildiniz. Anahtarlık kazandınız".format(x))
         elif(x==4):
             print("Tebrikerl {} denemede bildiniz. Kalem kazandınız".format(x))
         break    
    else:
      x+=1
      print("Sayı : {} \nKalan Hakkınız: {}".format(bs,-(x-5)))
             
         
             
