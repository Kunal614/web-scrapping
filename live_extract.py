import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent



def get_score(url,ua,res,match):
    res=requests.get(url,headers=ua)
    soup=BeautifulSoup(res.text,'html.parser')
    score=soup.find_all('description')
    enter=input("You want a cricket score press Y or N :: ")
    match=" "
    while enter!='N':
        if enter=='Y':
            for match in score:
                print(match.get_text())
                continue
    
        
        enter=input("You want a cricket score press Y or N")
    
   

    
if __name__=="__main__":
    ua={"UserAgent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}
    url="http://static.cricinfo.com/rss/livescores.xml"
    res=""
    match=" "
    get_score(url,ua,res,match)