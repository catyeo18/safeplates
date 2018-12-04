from selenium import webdriver
from bs4 import BeautifulSoup
from functools import reduce

def returnSoup(link):
	print("Entered function")
	
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	browser = webdriver.Chrome(chrome_options=options)

	browser.get(link)
	browser.implicitly_wait(50)

	# parse the html using beautiful soup and store in variable `soup`
	soup = BeautifulSoup(browser.page_source, 'html.parser')
	
	browser.close()

	# print(soup)
	return soup

def goodRestaurants(restaurants, user_restrictions):
	safeRestaurants = []
	for restaurant in restaurants:
		safeItems = [restaurant[1][item] for item in restaurant[1] if safeFood(item, user_restrictions)]
		# print(safeItems)
		if len(safeItems) >= 5:
			# print(restaurant[0]["name"])
			safeRestaurants.append((restaurant[0], safeItems))
	safeRestaurants.sort(key= lambda x: len(x[1]))
	# for restaurant in safeRestaurants:
	# 		for item in restaurant[1]:
	# 			print("You can eat " + item + " from " + restaurant[0]["name"])

	return safeRestaurants
		
def safeFood(item, user_restrictions):
	return reduce(lambda x, y: x and (y not in item.lower()), user_restrictions, True)
		# if safe:
		# 	goodRestaurants.append(restaurant)

	# return goodRestaurants