# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 22:10:24 2023

@author: ekrem
"""

print("************Kimlik Doğrulama**************")

ad=input("Adınızı Giriniz:")
soyad=input("Soyadınızı giriniz:")
annekızlıksoyadı="göksel"
harf=input("Anne kızlık soyadınızın 5. harfini giriniz")
if(annekızlıksoyadı[4]==harf.lower()):
    print("Giriş Başarılı")
else:
    print("bilgileri kontrol ediniz")    