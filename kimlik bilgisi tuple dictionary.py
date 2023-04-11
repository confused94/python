# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:57:02 2023

@author: ekrem
"""

#ad soyad tel mail bilgisini tutabildiğimiz demet ve sözlük kullanarak pro.
ad=input("Adınız : ")
soyad=input("Soyadınız : ")
tel=input("Telefon Numaranız : ")
mail=input("Mail Adresiniz : ")
#tuple ile bilgileri değişmez şekilde ve yeni bir bilgi oluşturmamak için kaydettik
bilgiler=(ad,soyad,tel,mail)
#sözlük yapısı oluşturuyoruz
bilgi={"isim":bilgiler[0],
       "soyad":bilgiler[1],
       "telefon":bilgiler[2],
       "mail":bilgiler[3]}
#bilgileri ekrana basma
print("""Öğrenmek istediğiniz bilgiyi aşağıda görmüş olduğunuz seçeneklerden
      birini yazarak öğrenebilirsiniz""")
print(" isim\n soyad\n telefon\n mail ")
sorgu=input("Hangisini öğrenmek istiyorsunuz:")

if sorgu in bilgi:
    print(sorgu,"\t",bilgi[sorgu])


    
    
   



    



        


    



