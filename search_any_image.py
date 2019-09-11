import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import sys
from selenium import webdriver
import os
file1=" "
def create_dir(path):
    dir='prnimage'
    path=os.path.join(path,dir)
    os.makedirs(path, exist_ok=True)

    
def extract_data(url,ua,images):
    
    res=requests.get(url,headers=ua).text
    soup=BeautifulSoup(res,'html.parser')
    images1=soup.find_all('img')
    print(images1)
    print("\n")
    
   
    size=len(images1)
    print(size)
    print("Downloading.....")
    for i in range(size):
        imgurl=images1[i].get('src')
        res1=requests.get(imgurl)
        print("%s"%imgurl)
        file1=open(os.path.join('prnimage',os.path.basename(imgurl)),'wb')

        for j in res1.iter_content(100):
           
            file1.write(j)
        file1.close()  
        
        
        




if __name__=="__main__":
    print("Search 20 images ")
    ua={"UserAgent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}
    
    url="https://www.google.com/search?q="
    search=input("whom image : ")
    url1="&client=ubuntu&channel=fs&sxsrf=ACYBGNQv5Wx7c9Dl5zaPYuVNc6dLxnaByg:1568174616717&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjEp-bX8cfkAhXFgeYKHasuAjoQ_AUIEygC&biw=1120&bih=565"
    url+=search+url1
    path="/home/iiitk/Desktop/python"
    images=""
    create_dir(path)
    extract_data(url,ua,images)
