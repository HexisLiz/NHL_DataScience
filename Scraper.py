# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:28:10 2024

@author: Mads Benjamin
"""

import urllib
import time

YearsToScrape = (2025 - 1980)  # This calculates 45, representing 45 years

for i in range(YearsToScrape):
    year = 1980 + i  # Current year in the loop
    url = "https://www.hockey-reference.com/leagues/NHL_" + str(year) + "_games.html"
    
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)  # Open the URL

        if response.status == 200:  # Check if status code is 200 (OK)
            hockeyscores = response.read().decode('utf-8')  # Decode the HTML content
            
            # Save the content to a file
            with open("NHL_" + str(year) + ".html", "w", encoding="utf-8") as file:
                file.write(hockeyscores)
            print("File for year " + str(year) + " saved successfully.")

            # Wait for 3 seconds between requests
            time.sleep(3)
        else:
            print("Failed to retrieve the page for year " + str(year) + ". Status code:", response.status)
    
    except:
        print("An error occurred for year " + str(year))



