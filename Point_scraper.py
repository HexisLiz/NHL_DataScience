#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#"""
#Created on Thu Nov 14 20:30:11 2024

#@author: madsbenjamin
#"""

import urllib
import time
import os
from bs4 import BeautifulSoup

#___________________________________________________________________________________________________________
#Scraper for points (Som jo self ikke er # mål :C)
files = os.listdir ("NHL")
YearsToScrape = (2025 - 1980)
n = 0
    
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
    
#___________________________________________________________________________________________________________   
#Her finder vi team navn til navngivnign af filer.  
    for row in rows: #Vi mangler spil dato-data som er stored i header værdi.
       try:    
           gamedata = row.findAll ("td")
           hometeam_name = gamedata[3].text.strip()
          
           gamedate_data = row.findAll ("th") #th er TableHeader
           gamedate = gamedate_data[0].text.strip()
           
           hyperlink = row.find ("a")
           time.sleep(3)        
           
           if hyperlink:
               scorelink = hyperlink.get("href")
               url = "https://www.hockey-reference.com" + str(scorelink)
               
               try:
                   request = urllib.request.Request(url)
                   response = urllib.request.urlopen(request)  # Open the URL
         
                   if response.status == 200:  # Check if status code is 200 (OK) Burde være tidligere i koden?? error 429
                       hockeyscores = response.read().decode('utf-8')  # Decode the HTML content
                       
                       with open("NHL_score_" + str(gamedate)+ " " + str(hometeam_name) + ".html", "w", encoding="utf-8") as file:
                           file.write(hockeyscores)
                       print("File for year " + str(gamedate) +str(hometeam_name)+ " saved successfully.")
           
                   else:
                       print("Failed to retrieve the page for year " + str(year) + ". Status code:", response.status)
               
               except:
                   print("An error occurred for year " + str(year))

          
           
       except: 
            print ("error09")
