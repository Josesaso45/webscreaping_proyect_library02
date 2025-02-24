import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime 

url = 'https://books.toscrape.com/'

response = requests.get(url)

#Listas par almacenar los datos
titles = []
prices = []
stock = []
urls = []
genres = []

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find('li',class_= 'col-xs-6 col-sm-4 col-md-3 col-lg-3')

    for book in books:
        #Obtiene el titulo del libro
        h3_title = book.find('h3')
        title = h3_title.find('a', href= True).getText()
        titles.append(title)

        '''
        #Obtiene el precio del libro
        price = book.find('p', class_='price_color').getText()
        prices.append(price)

        #Obtiene el stock del libro
        stock = book.find('p', class_='instock availability').getText()
        stock.append(stock)

        #Obtiene el genero del libro
        genre = book.find('p', class_='genre').getText()
        genres.append(genre)

        #Obtiene la url del libro
        url = book.find('h3').find('a').get('href')
        urls.append(url)
        '''
    #Imprime los titulos de los libros
    for title in titles:
        print(title)

    
    
else:
    print("Error en la petición GET")


    