
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
        table = soup.findAll("table")
        table_season = table [0]
        table_playoff = table [1]
    except: 
        print ("error in file", file)
        
    try: #2005 luckout
        rows = table_season.findAll ("tr")
    except:
       print ("error in table_Season.findAll occured")
#________________________________________________________________________________________________________________             
    for row in rows : #gamedate og link 
        gamedate_data = row.findAll ("th") #th er TableHeader
        try:
            gamedate = gamedate_data[0].text.strip() #strip fjerner alt andet en teksten vi er sulten efter
            hyperlink = gamedate_data[0].find("a")
        except:     
            print ("error in find a")
        
        try:
                link = hyperlink.get ("href") #https://www.crummy.com/software/BeautifulSoup/bs4/doc/ Her er hvordan man bruger "href".
                #print("Link:", link)
        except:
            print ("error in find hyperlink")
#________________________________________________________________________________________________________________
        try: 
            text_points = open ("link", "r").read()
            print (text_points)
        except: 
            print ("error opening points files")
        
    
    
    
    
    
    
    
    
    
    for row in rows: # Alle table data værdier
       gamedata = row.findAll ("td")    

      
       try:
       
          gamedate = gamedate
          visitor_team = gamedata[1].text.strip()
          visitor_goals = gamedata[2].text.strip()
          home_team = gamedata[3].text.strip()
          home_goals = gamedata[4].text.strip()
          visitor_points = 1 
          home_points = 1
          attendance = 1
          gamelenght = 1
          game_decided_by = 1 
          seasonality = 1
          
          
          df.append([visitor_team,visitor_goals,home_team,home_goals])

       except:
          print ("appending error")







df = pandas.DataFrame(df,columns = ['gamedate','visitor_team','visitor_goals','home_team','home_goals', "visitor_points", "home_points" ,"attendance" , "gamelenght", "game_decided_by", "seasonality" ])
df.to_csv("NHL",file,".csv", index=False, encoding='utf-8')








