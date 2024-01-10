# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 15:11:24 2023

@author: Ekrem Burak Onuş
"""
try:
    def hesap(yiyecek,icecek,tatlı):
        yiyecekler={"01":70,
                    "02":24,
                    "03":20,    
                    "04":60   
                   }
        yiyecek=yiyecekler[yiyecek]
                
        icecekler={ "01":15,
                    "02":8,
                    "03":12,    
                    "04":5    
                  }
        
        icecek=icecekler[icecek]
        tatlılar= { "01":30,
                    "02":50,
                    "03":35,    
                    "04":20    
                  }    
        tatlı=tatlılar[tatlı]
        
                    
            
        print("Yiyecekler",10*"-",yiyecek,"TL",end="\n")
        print("İçeçekler",10*"-",icecek,"TL",end="\n")
        print("Tatlılar",10*"-",tatlı,"TL",end="\n")
        return print(yiyecek+icecek+tatlı)
        
    print("Lokanta Menüsü")
    print("01 İskender","02 Cantık","03 Çorba","04 Pideli Köfte",sep="\n",end="\n")
    yiyecek=input("Lütfen İStediğiniz ürünün kodunu girin(örn 01) : ")
    if (yiyecek=="01" or yiyecek=="02" or yiyecek=="03" or yiyecek=="04"):
        print("Eklendi")
    else:
        print("Böyle bir ürün bulunmamaktadır..")
    print("01 Kola ","02 Ayran","03 Fanta","04 Meyve Suyu",sep="\n",end="\n")    
    icecek=input("Lütfen İStediğiniz ürünün kodunu girin(örn 01) : ")
    if (icecek=="01"or icecek=="02"or icecek=="03" or icecek=="04"):
        print("eklendi")
    else:
        print("Böyle bir ürün bulunmamaktadır")    
    print("01 Sütlaç","02 Kazandibi","03 Künefe","04 Magnolya",sep="\n",end="\n")
    tatlı=input("Lütfen İStediğiniz ürünün kodunu girin(örn 01) : ")    
    if (tatlı=="01"or tatlı=="02"or tatlı=="03" or tatlı=="04"):
        print("eklendi")    
    else:
        print("Böyle bir ürün bulunmamaktadır..")
    
    hesap(yiyecek,icecek,tatlı)
except KeyError:
    print("Lütfen kodları doğru giriniz...!!")        

input()