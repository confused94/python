# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 00:43:16 2023

@author: Ekrem Burak Onuş
"""
import random
deger=1
hak=5
def tahminoyunu(sayi):
    
    tahmin=random.randint(1, 5)
    if tahmin==sayi:
        print("Tebrikler bildiniz..")
        return 0
    else:
        print("Malesef bilemediniz Sayı ",tahmin)
        return 1
            
print(5*"*","Sayı Tahmin Etme Oyununa Hoşgeldiniz",20*"*")
print("Sayı tahmin etmede 5 hakkınız bulunmaktadır")
while deger==1:
        deger=tahminoyunu(int(input("Lütfen sayı tahmininde bulunun")))
        hak-=1
        if hak==0:  
            print("tekrar denemek ister misiniz E'ye basın")
            giris=input("")
            if giris.lower()=="e":
                deger=1
            else:
                deger=0    
        
        
        
         
                  
    

    
    
    
          

           
    
    
        

        