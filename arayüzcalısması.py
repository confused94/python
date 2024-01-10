# -*- coding: utf-8 -*-
"""
Created on Thu May  4 22:51:57 2023

@author: Ekrem Burak Onuş
"""

import tkinter as tk

pencere=tk.Tk()
pencere.title("Ekremin Programı")
pencere.geometry("800x800")
pencere.configure(background="light blue")


baslik=tk.Label(text="Apartman",bg="black",fg="white",font="Arial 15 bold")
baslik.pack(side="top")

def yonetici():
    
    tc=tk.Label(text="TCKN NO",bg="light blue",fg="red",font="Times 10 bold")
    tc.place(relx=0.4,rely=0.2)
    tc_enter=tk.Entry()
    tc_enter.place(relx=0.45,rely=0.2)
    sifre=tk.Label(text="Şifre",bg="light blue",fg="red",font="Times 10 bold")
    sifre.place(relx=0.4,rely=0.23)
    sifre_enter=tk.Entry(show="*")
    sifre_enter.place(relx=0.45,rely=0.23)
    
def kullanici():
    isim=tk.Label(text="İsim",bg="light blue",fg="red",font="Times 10 bold")
    isim.place(relx=0.4,rely=0.2)
    isim_enter=tk.Entry()
    isim_enter.place(relx=0.45,rely=0.2)
    sifre=tk.Label(text="Şifre",bg="light blue",fg="red",font="Times 10 bold")
    sifre.place(relx=0.4,rely=0.23)
    sifre_enter=tk.Entry(show="*")
    sifre_enter.place(relx=0.45,rely=0.23)



yonetici_giris = tk.Button(pencere, text="Yönetici Giriş", fg="red", bg="silver", font="Arial 10 bold", width=10, height=3,command=yonetici)
yonetici_giris.place(relx=0.4, rely=0.5, anchor="center")

kullanici_giris = tk.Button(pencere, text="Kullanıcı Giriş", fg="red", bg="silver", font="Arial 10 bold", width=10, height=3,command=kullanici)
kullanici_giris.place(relx=0.6, rely=0.5, anchor="center")















pencere.mainloop()
