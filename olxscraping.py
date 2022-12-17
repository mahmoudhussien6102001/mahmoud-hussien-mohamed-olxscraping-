import requests
from bs4 import BeautifulSoup

link=[]
price=[]
title=[]
picture=[]
c_link=0
c_price=0
c_picture=0
c_title=0
try:
    for a in range(1,30):
        url=f"https://www.olx.com.eg/vehicles/?page={a}"
        page=requests.get(url)
        soup=BeautifulSoup(page.content,'html.parser')
        #print(soup.prettify())
        print('*********')
        titles=soup.find_all('div',{'class':'a52608cc'})
        for i in range(len(titles)):

            title.append(titles[i].a.attrs['title'])
            c_title+=1
        print(title)
        print('#########')
        links=soup.find_all('div',{'class':'a52608cc'})
        for i in range(len(links)):

             link.append(links[i].find("a").attrs['href'])
             link[i]="https://www.olx.com.eg/en"+link[i]
             c_link+=1
        print(link)
        print('&&&&&&&&&&')


        prices=soup.find_all('div',{'class':'_52497c97'})
        for i in range(len(prices)) :
              price.append(prices[i].text)
              c_price+=1
        print(price)
        print("//////////////")
        pictures=soup.find_all('div',{'class':'ee2b0479'})
        for i in range(len(pictures)):
            picture.append(pictures[i].img.attrs['src'])
            c_picture+=1
        print(picture)
        print('++++++++++++++++')


        for x in range(c_link):
            print("name:",title[x])
            print(" ")
            print("price:", price[x])
            print(" ")
            print("picture link:", picture[x])
            print(" ")
            print("link on website", link[x])
        print("***************")
except:
    print("error the developer change the page html")
    '''''
    print("pic=",c_picture)
    print("price=",c_price)
    print("link=",c_link)
    print("title=",c_title)
    '''''
