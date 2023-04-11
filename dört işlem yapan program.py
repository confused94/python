# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 19:22:13 2023

@author: ekrem
"""
while True:
     print("Hesap Makinesi")


     print(50*"-")
     print("Tuş Atamaları\nTopla +\nÇıkar -\nÇarp *\nBöl /\nÇıkış c")
#Kullanıcıdan deger alnma
     s1=int(input("Birinci sayı :"))
     s2=int(input("İkinci sayı  :"))
     tus=input("İşlem seçiniz :")

#dört islem degiskenleri

     topla=s1+s2
     cikar=s1-s2
     carp=s1*s2
     bol=s1/s2
     

#Kontrol edip ekrana basma
     if(tus=="+"):
             print("{}+{}={}".format(s1,s2,topla))
     elif(tus=="-"):
             print("{}-{}={}".format(s1,s2,cikar))
     elif(tus=="*"):
             print("{}x{}={}".format(s1,s2,carp))
     elif(tus=="/"):
             print("{}/{}={}".format(s1,s2,bol))    
     elif(tus=="c"):
         break
             