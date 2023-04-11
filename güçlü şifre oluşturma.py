# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 19:28:56 2023

@author: ekrem
"""
#Şifre Tanımı
print(20*"-","\n Oluşturulacak şifre\n Büyük Harf\n Küçük Harf\n Özel Karakter\n Rakam\n 8 karakter\n uzunluğu içermelidir.\n",end=20*"-")


sifre=input("\n Şifre :")

bharf="x"
kharf="x"
ozel="x"
rakam="x"   
sorgu="✓"
kontrol=True 
#Şifrenin sorgulanması
if len(sifre)>6 and len(sifre)<10:
   
    for i in sifre:
      
      if i.isnumeric():
          rakam="✓"
      elif i.isupper():
          bharf="✓"    
      elif i.islower():
          kharf="✓"    
      elif i.isascii():
          ozel="✓"
else:
    print("Şifre 7 ile 9 karakter arasında olmalıdır")
    kontrol= False          
#Çıktılar
if(sorgu==rakam and sorgu==bharf and sorgu==kharf and sorgu==ozel):
          print("Güçlü Şifre Oluşturuldu")
elif kontrol:
          print(" Rakam {}\n Büyük Harf {}\n Küçük Harf {}\n Özel Krktr {}".format(rakam,bharf,kharf,ozel))
    
    
   

    

           
                



    


            
            
        