from email import header
from bs4 import BeautifulSoup
import requests
import re




#The header may need to be changed depending on your chrome browser
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
#URL can be changed
URLtoObtain = "https://www.sfml-dev.org/tutorials/2.5/window-window.php"

#getting the html
myHumblestOfRequests = requests.get(URLtoObtain,headers = headers)
fileText = myHumblestOfRequests.text

#creating a temporary html file
f = open("temp.html", "w")
f.write(fileText)
f.close()




print('you now have a webpage :]')
