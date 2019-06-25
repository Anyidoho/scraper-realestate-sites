from bs4 import BeautifulSoup
import requests
import csv


#requests for sending http requests as well as receive http response
#beautiful for pulling data out of html and xml files

#pages from which we want our files
pages = list(range(1,25))

for page in pages:
    #sends a get request to the url
    source = requests.get(f'https://www.property24.com/to-rent/camps-bay/cape-town/western-cape/11014/p{page}').text #parses response as a string so we can manipulate


    #We're using the lxml parser but we could also use the html5lib
    rental_page = BeautifulSoup(source,'lxml')

    #Create an empty csv file
    csv_file = open(f'property24_{page}.csv', 'w')

    #write data to csv file
    csv_writer = csv.writer(csv_file)

    #Headers for our csv
    csv_writer.writerow(['Title', 'NumberOfBedrooms','Description','Currency', 'Price/Monthly'])


    for house in rental_page.find_all("span", class_="p24_content"):
        title = 'Property to rent in Camps Bay'
        #print(title)

        NumberOfBedrooms = house.find('span',class_="p24_title").text.strip()[0]
        #print(NumberOfBedrooms)

        Description = house.find('span',class_="p24_excerpt").text.strip()
        #print(Description)

        Currency = 'R'
        #print(Currency)

        price_string = house.find('span',class_="p24_price").text.strip()[1:]
        price_remove_comma = price_string.replace("&nbsp;","")

        try:
            price = int(price_remove_comma)
        except Exception as e:
            price = None
        print(type(price_remove_comma))



        #csv_writer.writerow([title, NumberOfBedrooms, Description, Currency, price])


    #csv_file.close()




