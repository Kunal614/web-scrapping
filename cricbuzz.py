import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import os

import time

def watch_score(url,ua,data,data1):
    i=1
    while(i>0):
        res=requests.get(url,headers=ua)
        soup=BeautifulSoup(res.content,'html.parser')
        
        info=soup.find(class_='cb-min-bat-rw').get_text()
        data=soup.find(class_='cb-col cb-col-100 cdb-min-hdr-rw cb-bg-gray').get_text()
        print(data)
        print(info)
        
        time.sleep(20)
        i+=1
        
       
        

    

    
    
    

if __name__=="__main__":
    ua={"UserAgent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    url="https://www.cricbuzz.com/live-cricket-scores/20719/eng-vs-aus-5th-test-the-ashes-2019"
    data=""
    data1=" "
    watch_score(url,ua,data,data1)