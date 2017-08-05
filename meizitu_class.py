#coding:utf-8

import requests
from bs4 import BeautifulSoup
import re
import os
class Mzitu():
    def request(self,url):
        User_Agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
        headers={'User-Agent':User_Agent}
        content=requests.get(url,headers)
    def mkdir(self,path):
        path=path.trip()
        isExists=os.path.exists(os.path.join("F:\mzitu"))
        if not isExists:
            print(u'建了一个名字叫做',path,u'的文件夹')
            os.makedirs(os.path.join("F:\mzitu",path))
            os.chdir(os.path.join("F:\mzitu",path))
            return True
        else:
            return False
    def html(self,href):
        html=self.request(href)
        max_span=BeautifulSoup(html.text,'lxml').find('div',class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1,int(max_span)+1):
            page_url=href+'/'+str(page)
            self.img(page_url)
    def img(self,page_url):
        img_html=self.request(page_url)
        img_url=BeautifulSoup(img_html.text,'lxml').find('div',class_='main-image').find('img')['src']
        self.save(img_url)
    def save(self,img_url):
        name=img_url[-9:-4]
        img=self.request(img_url)
        f=open(name+'.jpg','ab')
        f.write(img.content)
        f.close()


    def all_url(self,url):
        html=self.request(url)
        all_a=BeautifulSoup(html.text,'lxml').find('div',class_='all').find_all('a')
        for a in all_a:
            title=a.get_text()
            print(u'开始保存：',title)
            path=re.sub('[\/?:*"><]','_',title)
            self.mkdir(path)
            href=a['href']
            self.html(href)

mzitu=Mzitu()
url='http://www.mzitu.com/all/'
mzitu.all_url(url)