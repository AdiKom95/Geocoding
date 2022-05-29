# -*- coding: utf-8 -*-
"""
Skrypt geokodujący zgodnie z tabelą adresów podaną w .csv

"""

import os

os.chdir('D:\\Studia_gospodarka_przestrzenna\\_II semestr\\Praca magisterska\\Skrypt_geokodowanie')

print(os.getcwd())




""" 1.Otwarcie pliku .csv z adresami, wczytanie danych do pamięci operacyjnej"""

import pandas  as pd
import openpyxl

lekarze=pd.read_csv('lekarze_poz_2.csv', delimiter = ',')

lekarze.insert(4,'x',0)
lekarze.insert(5,'y',0)

lekarze_2=lekarze#lekarze_2=lekarze.head(10)

#lekarze_2.loc[0,'x']=12


""" 2.Wywołanie usługi geokodowania """


for j in range(len(lekarze_2)):

    ul=lekarze_2['Ulica_dom'][j]
    adres="https://services.gugik.gov.pl/uug/?request=GetAddress&address=Poznań,{ulica}".format(ulica=ul)
    
    
    import requests
    
    #url = 'https://services.gugik.gov.pl/uug/?request=GetAddress&address=Marki,Andersa%201'
    r = requests.get(adres)
    r.close()
    tekst = r.text
    
    
    pozycja_x=tekst.find('"x"')+1 #Funkcja find() zwraca pozycję pierwszego znaku w podanym wzorcu, a więc cudzysłowia
    pozycja_y=tekst.find('"y"')+1
    
    koniec_wsp_x = tekst[pozycja_x:].find('",') #pozycja znaku kończącego wsp x (liczona od pozycji_x)
    koniec_wsp_x_2 = pozycja_x+koniec_wsp_x
    
    koniec_wsp_y = tekst[pozycja_y:].find('",') #pozycja znaku kończącego wsp y (liczona od pozycji_y)
    koniec_wsp_y_2 = pozycja_y+koniec_wsp_y
    
    
    wsp_x=''
    
    for i in tekst[pozycja_x+4:koniec_wsp_x_2]:
        wsp_x=wsp_x+i
        
    
    wsp_y=''
    
    for i in tekst[pozycja_y+4:koniec_wsp_y_2]:
        wsp_y=wsp_y+i

    lekarze_2.loc[j,'x']=wsp_x
    lekarze_2.loc[j,'y']=wsp_y
    

lekarze_2.to_excel(r'lekarze_wsp.xlsx', index = True, header=True)

