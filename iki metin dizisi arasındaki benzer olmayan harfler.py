# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 00:15:30 2023

@author: ekrem
"""

metin1="ilsşdfmgdofmgcşolkfgndifgn"
metin2="mdfmgkrndskfngsdlkfslkdf"
fark=""
sonuc=""
for x in metin1:
    if(not x in metin2 and not x in fark):
        fark+=x
       
        
print(fark)        