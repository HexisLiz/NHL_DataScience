
import os 
import pandas 
from bs4 import BeautifulSoup

n=0

df = []

files = os.listdir ("NHL")

#Finder, åbner og gemmer tables for hver enkelt HTML fil: 
    
for file in files : #loop der går gennem hver fil i fil mappen
    text = open("NHL/"+file, "r").read() #Her skal den "read" for at åbne det som string
    soup = BeautifulSoup (text, features = "lxml")
    
    try:
        table = soup.findAll("table")#, {"class":"sortable stats_table now_sortable"})
        table_season = table [0]
        table_playoff = table [1]
    except: 
        print ("error in file", file)
        
        
    try: #der er en fejl i 2005 fordi der var locout i hockey? XD
        rows = table_season.findAll ("tr")
    except:
       print ("An error in table_Season.findAll occured")
             
    
 #Scrape datoen for kampen da det er en tableheader
    for row in rows : 
        gamedate_data = row.findAll ("th") #th er TableHeader
        
        if gamedate_data:
            gamedate = gamedate_data[0].text.strip() #strip fjerner alt andet en teksten vi er sulten efter
            print("Game Date:", gamedate)
            
            hyperlink = gamedate_data[0].find("a")
            
        if hyperlink:
                link = hyperlink.number.strip()# Get the href attribute from the <a> tag
                print("Link:", link)
        
    
    
    
#Scraper alt andet data i table ved table data
#Problem med at td har data punkter der faktisk er headers.... 
     
    for row in rows: #Vi mangler spil dato-data som er stored i header værdi.
       gamedata = row.findAll ("td")    
       lenght = (len(gamedata))

      
       try: #der er en table data "td" pr år der mangler data, gad vide hvor den er måske headers?? 
          visitor_team = gamedata[1].text.strip()
          visitor_goals = gamedata[2].text.strip()
          home_team = gamedata[3].text.strip()
          home_goals = gamedata[4].text.strip()
          df.append([visitor_team,visitor_goals,home_team,home_goals])
         
       except:
          n = n+1
          print ("error", n)
          print (file)
#Vi skal også have Playoff data med bare fordi det er 4fun? XD

#Her finder vi playoff tabel 
    table_2 = soup.findAll("table")#, {"class":"sortable stats_table now_sortable"}
    table_playoff = table_2[1]
    

#playoff data
    for row in rows : 
        gamedate_data_playoff = row.findAll ("th") #th er TableHeader
        lenght_playoff = (len(gamedate_data))
        gamedate_playoff = gamedate_data[0].text.strip() #strip fjerner alt andet en teksten vi er sulten efter
       
        
    for tableheader in table:
        hyperlink = row.findAll ("a")
        print (hyperlink.text.strip)







#Nu skal det hele gemmes i CSV filer. 


df = pandas.DataFrame(df,columns = ['gamedate','visitor_team','visitor_goals','home_team','home_goals'  ])
df.to_csv('shootings.csv', index=False, encoding='utf-8')

print (df)









