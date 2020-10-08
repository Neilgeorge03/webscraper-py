from selenium import webdriver
import pandas as pd
import time
from datetime import datetime
import requests

PATH = ""   #Location of your Chrome Webdriver
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = webdriver.Chrome(PATH, chrome_options=options)
#Removes the the new pop up whenever selenium opens Chrome

Data = {'Count':'','Time':'','Weekday':''}  #names of every column 

#If ever I need to make a new csv file
conter= []
temps= []
semaine= []
#names of the lists containing the data for each column 
'''
main = pd.read_csv() #import already existing dataset with same column names
df = pd.DataFrame(main, columns=['Count', 'Hour', 'Weekday'])
temps= df.Hour.to_list()
semaine= df.Weekday.to_list()
#convert dataset into list for easier data adding
'''
def Countdown(t):
    time.sleep(t) 
    Scrap() #website link
def Scrap(URL):
    try:
        
        driver.get(URL) #open website
        time.sleep(5)   #wait time if the website has fancy JS that makes it impossible to get the data immediately once opening the website
        main = (driver.find_element_by_id()) #name of the id you're looking for(you can look for other things such as classes but google that)
        conter.append(main.text) #append the info
        semaine.append(datetime.now().strftime("%A")) #current date
        temps.append(datetime.now().strftime("%H:%M:%S"))   #current time 
        Data['Count']=conter
        Data['Hour']=temps
        Data['Weekday']=semaine
        #incorportate the data into a dictionary 
        df = pd.DataFrame(Data, columns=['Count', 'Hour', 'Weekday']) 
        #convert to pandas dataframe
        df.to_csv() #location to where to save scrapped data
        print(df)   #print the data you got
    except requests.exceptions.ConnectionError:
        requests.status_code = "Connection refused"
        #make sure the code doesn't crash
    URL = ''
    Countdown(600) #cooldown if you want one 

Countdown(0)    #to start the code    
