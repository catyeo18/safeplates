from selenium import webdriver
from bs4 import BeautifulSoup

def returnSoup(link):
	print("Entered function")
	browser = webdriver.Chrome()

	browser.get(link)
	browser.implicitly_wait(30)
	# browser.close()

	# parse the html using beautiful soup and store in variable `soup`
	soup = BeautifulSoup(browser.page_source, 'html.parser')
	
	# browser.quit() 
	# print(soup)
	return soup