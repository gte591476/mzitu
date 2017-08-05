# mzitu
爬取http://www.mzitu.com上妹子图片

python3：requests/Beautifulsoup
爬虫入口：http://www.mzitu.com/all/

bs4:
img_url=img_soup.find('div',class_='main-image').find('img')['src']