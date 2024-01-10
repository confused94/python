# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:11:08 2023

@author: Ekrem Burak Onuş
"""
import datetime


def bilethesap(yas,mesafe):
     if yas<18:
        bilet=25
     elif yas>18 and yas<30:
        bilet=50
     else:
        bilet=40
     if mesafe<=2:
         bilet=bilet+20
     else:
         bilet=bilet+40
     return bilet    
def bilettarih():
   
    tarih=datetime.datetime.now()
    return tarih.strftime("%Y.%m.%d %H:%M")

def kisibilgisi():
    ad=input("İsminizi giriniz:")
    soyad=input("Soyadınızı giriniz:")
    yas=int(input("Yaşınızı giriniz:"))
    print("1-Bursa-İstanbul","2-Bursa-İzmir","3-Bursa-Eskişehir","Hangi bileti almak istiyorsunuz(örn 1)" ,sep="\n",)
    mesafe=int(input("Giriniz: "))
    if mesafe==1:
        sehir="Bursa_İstanbul"
    elif mesafe==2:
        sehir="Bursa-İzmir"
    else:
        sehir="Bursa-Eskişehir"
    biletler={1:2,
              2:4,
              3:2
             }
    zaman=biletler[mesafe]    
    bilet=bilethesap(yas,zaman)
    tarih=bilettarih()           
    return print("Hoşgeldiniz {} {}\nBiletinizi {} tarihli {} arası {}TL tutarında satın aldınız. İyi Yolculuklar".format(ad,soyad,tarih,sehir,bilet))


kisibilgisi()
    
input()