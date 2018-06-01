import requests
import os
import urllib.request
from bs4 import BeautifulSoup
import time
from selenium import webdriver
header = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3239.132 Safari/537.36'
}

if __name__ == "__main__":
    year = '2017'
    max = 26
    for idx in range(1,max+1):
        url = 'https://auto.naver.com/car/mainList.nhn?mnfcoNo=0&modelType=OS&order=0&importYn=Y&saleType=-1&lnchYY='+year+'&page='+str(idx)
        html = requests.get(url)
        bs4 = BeautifulSoup(html.text,'lxml')
        modelLst_lis = bs4.find('ul',class_='model_lst ').find_all('li')
        for li in modelLst_lis:
            try:
                print(li.find('img')['src'])
                pic_url = li.find('img')['src']
                pic_title = li.find('img')['alt']
                dirname = "./pics/"
                if not os.path.exists(dirname):
                    os.makedirs(dirname)
                fileurl = dirname + str(pic_title.strip()) +".jpg"
                urllib.request.urlretrieve(pic_url, fileurl)
            except:
                pass
        time.sleep(2)