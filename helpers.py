from selenium import webdriver
from bs4 import BeautifulSoup
from functools import reduce

# Function to scrape HTML from a webpage
# Parameters: a URL string
def returnSoup(link):
	print("Entered function")
	
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	browser = webdriver.Chrome(chrome_options=options)

	# Load webpage
	browser.get(link)
	browser.implicitly_wait(50)

	# Parse the HTML using BeautifulSoup and store in variable `soup`
	soup = BeautifulSoup(browser.page_source, 'html.parser')
	
	# Close webpage
	browser.close()

	return soup

# Function to return an array of restaurants that satisfy user's dietary restrictions
# Parameters: array of restaurants, array of user's dietary restrictions
def goodRestaurants(restaurants, user_restrictions):
	safeRestaurants = []
	for restaurant in restaurants:
		# Store all menu items that are safe for user to eat
		safeItems = [restaurant[1][item] for item in restaurant[1] if safeFood(item, user_restrictions)]
		
		if len(safeItems) >= 5:
			safeRestaurants.append((restaurant[0], safeItems))

	# Sort restaurants by how many safe items they have
	safeRestaurants.sort(key= lambda x: len(x[1]))

	return safeRestaurants
		
# Function to return whether a menu item is in the user's dietary restrictions
def safeFood(item, user_restrictions):
	return reduce(lambda x, y: x and (y not in item.lower()), user_restrictions, True)