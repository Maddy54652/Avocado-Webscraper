from email import header
from bs4 import BeautifulSoup
import requests
import re


def introScreen():
    #print new line
    print('Hello! Welcome to the Avocado Webscraper. This is version 1.0.1 Created by Maddy Henderson')

def getURL():
    #ask for url
    userURL = input('please enter the url of the webpage you would like to obtain:')
    return userURL
    #return user input


introScreen()
#The header may need to be changed depending on your chrome browser
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
#URL can be changed
URLtoObtain = getURL()

#getting the html
myHumblestOfRequests = requests.get(URLtoObtain,headers = headers)
fileText = myHumblestOfRequests.text

#creating a temporary html file
f = open("temp.html", "w")
f.write(fileText)
f.close()




print('you now have a webpage :]')
