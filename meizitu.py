# coding:utf-8

import requests
from bs4 import BeautifulSoup
import os
User_Agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
headers={'User-Agent':User_Agent}
url='http://www.mzitu.com/all'

start_html=requests.get(url,headers=headers)

soup=BeautifulSoup(start_html.text,'lxml')
a_list=soup.find('div',class_='all').find_all('a')
for a in a_list:
    title=a.get_text()
    path=str(title).strip()
    isExists=os.path.exists(os.path.join("F:\mzitu",path))
    if not isExists:
        os.makedirs(os.path.join("F:\mzitu",path))
    else:
        pass
    os.chdir("F:\mzitu\\"+path)
    href=a['href']
    html=requests.get(href,headers=headers)
    html_soup=BeautifulSoup(html.text,'lxml')
    max_span=html_soup.find('div',class_='pagenavi').find_all('span')[-2].get_text()
    for page in range(1,int(max_span)+1):
        page_url=href+'/'+str(page)
        img_html=requests.get(page_url,headers)
        img_soup=BeautifulSoup(img_html.text,'lxml')
        img_url=img_soup.find('div',class_='main-image').find('img')['src']
        name=img_url[-9:-4]
        img=requests.get(img_url,headers)
        f=open(name+'.jpg','ab')
        f.write(img.content)
        f.close()
