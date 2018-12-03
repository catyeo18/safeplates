from selenium import webdriver
from bs4 import BeautifulSoup
from functools import reduce

def returnSoup(link):
	print("Entered function")
	
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	browser = webdriver.Chrome(chrome_options=options)

	browser.get(link)
	browser.implicitly_wait(30)

	# parse the html using beautiful soup and store in variable `soup`
	soup = BeautifulSoup(browser.page_source, 'html.parser')
	
	browser.close()

	# print(soup)
	return soup

def goodRestaurants(restaurants, user_restrictions):
	goodRestaurants = []
	for restaurant in restaurants:
		safeItems = [item for item in restaurant[1] if safeFood(item, user_restrictions)]
		# safe = False
		for item in safeItems:
			print("You can eat " + restaurant[1][item])
		
def safeFood(item, user_restrictions):
	return reduce(lambda x, y: x and (y not in item.lower()), user_restrictions, True)
		# if safe:
		# 	goodRestaurants.append(restaurant)

	# return goodRestaurants