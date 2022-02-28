# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 10:52:37 2022

@author: Joshua
"""
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# Get categories
my_url = 'http://books.toscrape.com/index.html'

## Open connection, grab page
uClient = uReq(my_url)

## Off load content into variable
page_html = uClient.read()

## Close connection
uClient.close()

## HTML parsing
page_soup = soup(page_html,"html.parser")

## Itemize the category filter
category = page_soup.find("ul",{"class":"nav nav-list"}).find("ul")

text = list(category.descendants)

genres_list = []

for i in range(2, len(text), 2):
    genres_list.append(text[i].strip())
    #print(text[i].strip())

categories = []

for i in genres_list:
    if i != '':
        categories.append(i)

## Hyphenate category entries so they are suitable for the url
i = len(categories)

for j in range(i):
    categories[j] = categories[j].replace(' ','-')  


## Url's must be all lowercase
for k in range(len(categories)):
    categories[k] = categories[k].lower()

## j is a dummy index so the url works properly
j = 2

## Create output file
filename = 'books_by_genre.csv'
f = open(filename, 'w')

headers = 'Genre, Title, Rating, Price \n'

f.write(headers)

# Scraping loop
for genre in categories:
    
    my_url = 'https://books.toscrape.com/catalogue/category/books/' + \
        genre + '_' + str(j) + '/index.html'

    uClient = uReq(my_url)

    page_html = uClient.read()

    uClient.close()

    page_soup = soup(page_html,"html.parser")
    
    page = page_soup.find("ul",{"class":"pager"})

    containers = page_soup.findAll("article",{"class":"product_pod"})
    
    ## Scraping loop. Obtains title, rating, and price
    for container in containers:
        
        print(my_url)
        
        title = container.div.a.img["alt"]
        
        rating = container.p["class"]
        rating.reverse()
        rating = ' '.join(rating)
        
        price_container = container.findAll("p",{"class":"price_color"})
        price_container = price_container[0].text
        price_container = price_container[1:]
        
        print('Genre: ' + genre)
        print('Title: ' + title)
        print('Rating: ' + rating)
        print('Price: ' + price_container)
        
        f.write(genre + ',' + title.replace(',',':') + ',' + rating + ',' + price_container + '\n')
        
    #print(type(page))
    
    # Find number of pages for the genre
    
    if page != None:
        
        #print('This genre: ' + genre + ' has multiple pages')
        
        page = page_soup.find("ul",{"class":"pager"}).find("li")
        
        text = list(page)
        
        page = [s.strip() for s in text]
        
        page = ''.join(page)
        
        page = page.split()
        
        ## We basically have a string of the form 'Page x of y' and want to isolate the y variable as an int.
        max_page = int(page[-1])
        
        print('Max page number is: ' + str(max_page))
        
        
        if max_page > 2:

            for num in range(2,max_page+1):
                    
                        my_url = 'https://books.toscrape.com/catalogue/category/books/' + \
                        genre + '_' + str(j) + '/page-' + str(num) + '.html'
                        
                        print(my_url)

                        uClient = uReq(my_url)

                        page_html = uClient.read()

                        uClient.close()

                        page_soup = soup(page_html,"html.parser")

                        containers = page_soup.findAll("article",{"class":"product_pod"})

                        for container in containers:
                            
                            print(my_url)
                            
                            title = container.div.a.img["alt"]
                            
                            rating = container.p["class"]
                            rating.reverse()
                            rating = ' '.join(rating)
                            
                            price_container = container.findAll("p",{"class":"price_color"})
                            price_container = price_container[0].text
                            price_container = price_container[1:]
                            
                            print('Genre: ' + genre)
                            print('Title: ' + title)
                            print('Rating: ' + rating)
                            print('Price: ' + price_container)
                            
                            f.write(genre + ',' + title.replace(',',':') + ',' + rating + ',' + price_container + '\n')
        
        elif max_page == 2: 
            
            my_url = 'https://books.toscrape.com/catalogue/category/books/' + \
            genre + '_' + str(j) + '/page-2.html'

            uClient = uReq(my_url)

            page_html = uClient.read()

            uClient.close()

            page_soup = soup(page_html,"html.parser")   

            containers = page_soup.findAll("article",{"class":"product_pod"})
            
            for container in containers:
                
                print(my_url)
                
                title = container.div.a.img["alt"]
                
                rating = container.p["class"]
                rating.reverse()
                rating = ' '.join(rating)
                
                price_container = container.findAll("p",{"class":"price_color"})
                price_container = price_container[0].text
                price_container = price_container[1:]
                
                print('Genre: ' + genre)
                print('Title: ' + title)
                print('Rating: ' + rating)
                print('Price: ' + price_container)
                
                f.write(genre + ',' + title.replace(',',':') + ',' + rating + ',' + price_container + '\n')

        else:
            continue
    
    j = j + 1
            
                        
f.close()
