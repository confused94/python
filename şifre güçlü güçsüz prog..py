# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 23:22:40 2023

@author: ekrem
"""

#şifre güvenli güvenli değil

print("Büyük Harf", "Küçük Harf", "Rakam" ,"Özel Karakter", "İçermelidir",sep="*\n")
bharf=0
kharf=0
rakam=0
ozel=0

while True:
    sifre=input("Şifre giriniz\t:")
    for x in sifre:
        if(x.isupper()):
            bharf+=1
        elif(x.islower()):
            kharf+=1
        elif(x.isnumeric()):
            rakam+=1
        else:
            ozel+=1
        
            
    break

if(bharf!=0 and kharf!=0 and rakam!=0 and ozel!=0 ):
    print("Şifre güçlü")


else:
    print("şifre güçsüz bilgileri kontrol edin")
    
      
            
            
    
    
    
    
    
    
