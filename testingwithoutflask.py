from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json, requests

# url = 'https://api.foursquare.com/v2/venues/explore'
link = 'https://www.grubhub.com/restaurant/sam-lagrassas-44-province-st-boston/68003?affiliate=1131&utm_source=foursquare-affiliate-network&utm_medium=affiliate&utm_campaign=1131&utm_content=68003'
browser = webdriver.Chrome()

# grabs URL of restaurant if possible
# link = data['response']['groups'][0]['items'][i]['venue']['delivery']['url']
# print(link)
# query the website and return the html to the variable html
#page = requests.get(link, timeout=5)
browser.get(link)
browser.implicitly_wait(30)
# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(browser.page_source, 'html.parser')
# print("Soup")
print(soup)
# diet = request.form.get("diet")
# print(soup.find_all("p"))
# for j in soup.find_all("meta"):
#   print(j)
    #print(j.text.strip.split)
    # if diet[0] not in i.text.strip.split:
    #   try:
    #     restaurants.append(data['response']['groups'][0]['items'][i]['venue'])
    #   except:
    #     print(i)

