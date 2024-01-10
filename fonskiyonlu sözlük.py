# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 12:55:59 2023

@author: Ekrem Burak Onuş
"""

def ingilizcesozluk(ingilizce):
    
    ingtr={"car":"araba",
            "house":"ev",
            "dog":"köpek",
            "money":"para",
          }
            
    print("İngilizce\tTürkçe\n{}\t\t{}".format(ingilizce,ingtr[ingilizce]))        
   
    
def turkcesozluk(turkce):
    
     tring={"araba":"car",
             "ev":"house",
             "köpek":"dog",
             "para":"money",
           }   
     print("Türkçe\tİngilizce\n{}\t{}".format(turkce,tring[turkce]))
     
     
ingilizcesozluk("car")
turkcesozluk("araba")