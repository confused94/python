# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 00:08:05 2023

@author: Ekrem Burak Onuş
"""

def hesapmakinesi(x,y):
    "Hesaplamak istediğiniz sayıları x ve y yerine atanacaktır"
    giris=input("""Lütfen yapmak istediğiniz işlemi yazıp entera basınız
                \rToplama +
                \rÇıkarma -
                \rÇarpma  *
                \rBölme   /
                \rÇıkış için Q ya basınız""")
     
    if giris=="+":
        print("Toplama işleminizin sonucu:\t",x+y)
    elif giris=="-":
        print("Çıkarma işleminizin sonucu:\t",x-y)
    elif giris=="*":
        print("Çarpma işleminizin sonucu:\t",x*y)
    elif giris=="/":
        print("Bölme işleminizin sonucu:\t",x/y)
    elif giris.lower()=="q":
        return print("Çıkış yapıldı")
    else:
        return print("Yanlış seçim yaptınız..!")
    
    



print(20*"*","Hesap Makinesi",20*"*")    
sayi1=int(input("Sayıyı giriniz: "))
sayi2=int(input("Sayıyı giriniz: "))
hesapmakinesi(sayi1,sayi2)          

    
    
    
    
    