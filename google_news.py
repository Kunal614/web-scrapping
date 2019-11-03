import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import webbrowser
import emoji

def Times_of_India(url,ua,url1):
    url1="https://timesofindia.indiatimes.com/india/"
    res=requests.get(url,headers=ua)
    soup = BeautifulSoup(res.content,'html.parser')
    data=soup.find_all(class_='w_tle')
    if len(data)>0:
        print("Total news avaliable :: ",len(data))
    if len(data)==0:
        return 0
    print("\n")
    for item in range(len(data)):
        print("\nNEWS : ",item+1,end="  ")
        data1=data[item].find('a')
        print(data1.get_text())
        
        bol=input("For more details ->(y) (y/n) :: ")
        if bol=='y':
            #print(data1.get('href'))
            url1+=data1.get('href')
            print("%s"%url1)

            webbrowser.open(url1)
    return len(data)        
          

def news_india(url, ua , url1):
    res=requests.get(url,headers=ua)
    soup = BeautifulSoup(res.content,'html.parser')  
    data= soup.find_all(class_='field-content') 
    if len(data)>0:
        print("\nTotal news avaliable :: ",len(data))
       
    for i in range(len(data)):
        data1=data[i].find_all('a')
        for j in range(len(data1)):
            print("\nNEWS ",i,end=" : ")
            print(data1[j].get_text())
            bol=input("\nFor more details ->(y) (y/n) :: ")
            if bol=='y' or bol == 'Y':
                data2 = data[i].find('a')
                url1=data2.get('href')
                #print("%s"%url1)
                webbrowser.open(url1)
            
        
        
    return len(data)    
        


url="https://timesofindia.indiatimes.com/india/"
ua={"UserAgent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}
num=input("Enter the state name or city name to get news : ")
url+=num
url1="https://timesofindia.indiatimes.com/india/"
url2="https://www.indiatoday.in/topic/"
url2+=num
url3 =""
print("Times of india")
print("Which news channel data would you prefer")
print("1. Times of india")
print("2. India's Today")
say = int(input())
if say==1:
    length = Times_of_India(url,ua,url1)
    if length==0:
        print("Sorry Here No News Available","\N{expressionless face}")
        print("\n")
        print("Would you like to go for India's Today (y/n):: ","\N{thinking face}",end="  ")
        speak= input()
        if speak=='y':
            news_india(url2,ua,url3)
        else:
            print("\nThank you","\U0001f600")    
elif say ==2:
   length=news_india(url2,ua,url3)
   if length==0:
       print("Sorry No news")
else:
    print("Sorry")       


    