from bs4 import BeautifulSoup
import requests
import csv




#requests for sending http requests as well as receive http response
#beautiful for pulling data out of html and xml files

#pages from which we want our files
pages = list(range(1,62))

for page in pages:
    #sends a get request to the url
    source = requests.get(f'https://meqasa.com/houses-for-rent-in-Cantonments?w={page}').text #parses response as a string so we can manipulate


    #We're using the lxml parser but we could also use the html5lib
    rental_page = BeautifulSoup(source,'lxml')

    #Create an empty csv file
    csv_file = open(f'meqasa_{page}.csv', 'w')

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
        print(Description)

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
        #print(price)



        csv_writer.writerow([title, NumberOfBedrooms, Description, Currency, price])


    csv_file.close()




