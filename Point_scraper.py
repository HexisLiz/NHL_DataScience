#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:30:11 2024

@author: madsbenjamin
"""

import urllib
import time
import os
from bs4 import BeautifulSoup

#___________________________________________________________________________________________________________
#Scraper for points (Som jo self ikke er # mål :C)
files = os.listdir ("NHL")
YearsToScrape = (2025 - 1980)
    
for file in files : 
    text = open("NHL/"+file, "r").read() 
    soup = BeautifulSoup (text, features = "lxml")

    try:
        table = soup.findAll("table")
        table_season = table [0]
        table_playoff = table [1]
    except:
        print("error1")
        
    try: 
        rows = table_season.findAll ("tr")
    except:
           print("error2")
    
    for row in rows :
        hyperlink = row.find ("a")
        
        if hyperlink:
            scorelink = hyperlink.get("href")

            year = 1980 + i  # Current year in the loop
            url = "https://www.hockey-reference.com" + str(scorelink)
            print (url)
                
            try:
                request = urllib.request.Request(url)
                response = urllib.request.urlopen(request)  # Open the URL
      
                if response.status == 200:  # Check if status code is 200 (OK) Burde være tidligere i koden?? error 429
                    hockeyscores = response.read().decode('utf-8')  # Decode the HTML content
                    
                    with open("NHL_score_" + str(year) + ".html", "w", encoding="utf-8") as file:
                        file.write(hockeyscores)
                    print("File for year " + str(year) + " saved successfully.")
        
                    time.sleep(3)
                else:
                    print("Failed to retrieve the page for year " + str(year) + ". Status code:", response.status)
            
            except:
                print("An error occurred for year " + str(year))
