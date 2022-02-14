from selenium import webdriver 
from bs4 import BeautifulSoup 
import time 
import csv
import pandas as pd
import requests

headers = ["Star", "Constellation", "Right_ascension", "Declination", "App._mag.","Distance","Spectral_type","Brown_dwarf","Mass","Radius","Orbital_period","Semimajor_axis","Ecc."] 
star_data = []
final_star_data = []
temp_list = [] 
new_star_data = []

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs" 
browser = webdriver.Chrome("chromedriver.exe") 
browser.get(START_URL) 
time.sleep(10)


soup = BeautifulSoup(browser.page_source, "html.parser")
star_table = soup.find_all('table')
table_rows = star_table[7].find_all('tr') 
    
            
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]
Lum = []

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][8])
    Radius.append(temp_list[i][9])

    df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star','Distance','Mass','Radius'])
    print(df2)

    df2.to_csv('brown_dwarfs.csv')
    print(f"{i} page done 1")
