# Automatyzacja procesu geokodowania


## Zasada działania

Skrypt ma za zadanie zautomatyzować geokodowanie adresów placówek lekarzy podstawowej opieki zdrowotnej znajdujących się na terenie Poznania. 

1. Zaczytywany jest plik .csv zawierający następujące informacje: Kolumna A - nazwa placówki; kolumna B - Miasto; kolumna C - adres (ulica + nr domu), kolumna D - telefon kontaktowy
 
2. Skrypt w pętli wywołuje Uniwersalną Usługę Geokodowania oferowaną przez GUGiK (http://services.gugik.gov.pl/uug/), sczytuje współrzędne geograficzne adresu ze zwróconego pliku JSON oraz dopisuje je do ramki danych obsługiwanej w pamieci operacyjnej

3. Finalnie lista placówek uzupełniona o współrzędnego geograficzne zapisywana jest w pliku .xlsx   

         
   
## Środowisko pracy

* Windows 10
* Anaconda -> IDE Spyder
* Python 3.7.4 -> Pakiety: os, pandas, openpyxl
