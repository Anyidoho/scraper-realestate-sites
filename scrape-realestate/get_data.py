from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://meqasa.com/apartments-for-rent-in-Cantonments?w=61').text #parses response as a string so we can manipulate


#We're using the lxml parser but we could also use the html5lib
rental_page = BeautifulSoup(source,'lxml')

#Create an empty csv file
csv_file = open(f'meqasa.csv', 'w')

#write data to csv file
csv_writer = csv.writer(csv_file)

#Headers for our csv
csv_writer.writerow(['Title', 'NumberOfBedrooms','Description','Currency', 'Price/Monthly'])





for house in rental_page.find_all("div", class_="mqs-prop-dt-wrapper"):
    title = house.h2.a.text
    #print(title)

    NumberOfBedrooms = title.split(" ")[0]
    #print(NumberOfBedrooms)

    Description = house.select('p')[1].text
    #print(Description)

    #remove span tags in paragraph tag
    house.select('p')[0].find('span').extract()
    house.select('p')[0].find('span').extract()

    Currency = house.select('p')[0].text.strip()[0]
    #print(Currency)

    price_string = house.select('p')[0].text.strip()[1:]
    price_remove_comma = price_string.replace(",",'')
    try:
       price = int(price_remove_comma)
    except Exception as e:
       price = None
    print(price)




    #csv_writer.writerow([title, NumberOfBedrooms, Description, Currency, price])


#csv_file.close()
