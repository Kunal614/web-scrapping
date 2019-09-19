import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import webbrowser


def news(url,ua,url1):
    url1="https://timesofindia.indiatimes.com/india/"
    res=requests.get(url,headers=ua)
    soup = BeautifulSoup(res.content,'html.parser')
    data=soup.find_all(class_='w_tle')
    print("Total news avaliable :: ",len(data))
    print("\n")
    for item in range(len(data)):
        print("\nNEWS : ",item+1,end="  ")
        data1=data[item].find('a')
        print(data1.get_text())
        bol=input("Would you like to go ahed regarding this (y/n) :: ")
        if bol=='y':
            #print(data1.get('href'))
            url1+=data1.get('href')
            print("%s"%url1)

            webbrowser.open(url1)
          
        
        


url="https://timesofindia.indiatimes.com/india/"
ua={"UserAgent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}
num=input("Enter the state name or city name to get news : ")
url+=num
url1="https://timesofindia.indiatimes.com/india/"
news(url,ua,url1)