from bs4 import BeautifulSoup
import requests
#from urllib.request import urlopen
import webbrowser
import sys
from fake_useragent import UserAgent
ua = UserAgent()
header={'user-agent':ua.chrome}
print("Googling.....")
res=requests.get('https://www.google.com/search?q='+ ' '.join(sys.argv[1:]),headers=header)
#res.raise_for_status()
file=open('project1a.html','wb') #only for knowing the class
for i in res.iter_content(10000):
    file.write(i)
soup= BeautifulSoup(res.text,'lxml')
linkele=soup.select('.eZt8xd')

num=min(5,len(linkele))
print(num)
for i in range(num):
    
    webbrowser.open('http://google.com' + linkele[i].get('href'))