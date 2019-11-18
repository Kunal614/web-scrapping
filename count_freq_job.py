#counting frequency of the job site roberthalf.com
#It will print the dictionary of the words with its frequency
#It will create a file where all the datas are stored the from the stored data it will calculate frequency
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
from lxml import html

def Remove_duplicate(list1):  #function for removing the duplicates
    new_list=[]
    for i in list1:
        if i not in new_list:
            new_list.append(i)
    return new_list


url="https://www.roberthalf.com/"
ua = {'UserAgent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}
res = requests.get(url,headers=ua)
soup = BeautifulSoup(res.content,'html.parser')

data = soup.find_all(class_='clearfix text-formatted field field--name-field-eck-carousel-text field--type-text-long field--label-hidden field__item')
my_file= open('my_file1.txt','w+')
for i in range(len(data)):
    my_file.write(data[i].get_text())

my_file.close()
new_file = open('my_file1.txt','r+')
word_list=[]
for i in new_file:
    word_list+=i.split()

string =""
for i in word_list:
    string+=str(i)
    string+=' '
    
new_list=Remove_duplicate(word_list)
word_dict={}
for word in new_list:
    k = string.count(word)
    word_dict[word]=k
print(word_dict)
 

