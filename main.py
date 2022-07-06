import requests
from lxml import html
import pandas as pd
from selenium import webdriver

#Main Link
main_link = 'https://www.encuentra24.com'

#Cont for while
cont = 0

#Variable to change the screen
direction = '/costa-rica-es/bienes-raices-venta-de-propiedades-casas/espectacular-casa-en-santa-barbara-heredia/17902711?list=category&catslug=bienes-raices-venta-de-propiedades-casas'

#Driver to open Firefox
browser = webdriver.Firefox(executable_path = '/Users/Denis Ugalde Meza/Documents/geckodriver')

#Open the first window to start the web scraping
browser.get('https://www.encuentra24.com/costa-rica-es/bienes-raices-venta-de-propiedades-casas/espectacular-casa-en-santa-barbara-heredia/17902711?list=category&catslug=bienes-raices-venta-de-propiedades-casas')

#Vectors to add to the data frame
ls = []
ls_2 = []

#While to check a specific number of properties
while(cont <= 1):

    # Making a GET request to main link + property direction
    r = requests.get(main_link + direction)

    #Take the content of the label
    tree = html.fromstring(r.content)

    #Look for the class that contains the "a" label of the next page
    data = tree.xpath("//*[@class = 'd3-detailpager__element d3-detailpager__element--next']/a")

    for i in data:
        #Assignation of the href that a contains to direction
        direction = i.get('href')
        #print(direction)

    #Take the values of the property fields
    tree_property = html.fromstring(r.content)
    #Separate the info in columns
    data_property = tree_property.xpath("//*[@class = 'col-800']/ul/li/span[1]")
    data_property_2 = tree_property.xpath("//*[@class = 'col-800']/ul/li/span[2]")

    for x in data_property:
        #Add to the ventor
        ls.append(x.text)

    for y in data_property_2:
        #Add to the vector
        ls_2.append(y.text)

    #Open the new direction
    browser.get(main_link + direction)
    #Cont + 1
    cont+=1

#print vectors
print(ls)
print(ls_2)


