# Safeplates
2018 Harvard CS50 Final Project: Catherine Yeo and Hannah Cole

## What Is Safeplates?
For individuals who have specific dietary restrictions, it is often difficult to find restaurants to go to that have available menu options that satisfy those restrictions. We created Safeplates to solve that problem.

**Safeplates** is a web app that gives local restaurant recommendations based on the dietary restrictions a user inputs. For example, if Alice can’t eat soy, the app would parse the menus of an inputted region's restaurants (of a specified radius) to determine which restaurants have the most soy-free options. 

## Design

### Summary: How does Safeplates work?
This web app is built and hosted locally. It uses [Foursquare](https://developer.foursquare.com/)'s API to provide restaurant data based on location and radius. That data includes links to restaurant menus on [Seamless](https://www.seamless.com/) and [GrubHub](https://www.grubhub.com/). After we have accessed the restaurant data from the API's data in a JSON format, we scrape the restaurant's online menu to access all menu items and their ingredients. We then parse through all the ingredients and return food items (and the restaurants they're from) that adhere to the user's dietary restrictions. 

### Languages, Libraries, and Frameworks Used

#### Back End
* Python
* Flask
* Selenium (for web scraping)
* Beautiful Soup (for web scraping)
* Headless (for web scraping)

#### Front End
* HTML
* CSS
* Javascript
* Jinja

### Detailed Walkthrough
The user begins by going to the form to which he/she can input dietary restrictions, location, and preferred radius. The dietary restrictions are selected through a list of checkboxes, so the user can check all that apply. The location input can take in an address, city, and/or zip code. Our JavaScript code in `form.html` ensures that the user must fill out both the location and preferred restaurant proximity.

Then, the user clicks the 'Submit' button to submit the form. Once that happens, the web app uses the inputted location and radius to access a list of restaurants given by Foursquare's API in JSON. The API provides us with information like name, cuisine, address, menu link, etc. It also stores the user's dietary restrictions in a set.

We iterate through that list of restaurants to look for the URLs of the restaurants' menus. Once the URL is found, the HTML is parsed and returned using the helper function `returnSoup` in `helpers.py`, which utilizes Beautiful Soup, Headless, and Selenium to scrape the webpage. Now, we look for specific HTML tags/attributes within that block of scraped HTML. Every menu item is embedded within HTML tags with class `menuItem-name`, so we iterate through the menu items to store its ingredients, which all have `itemprop` labelled with `description`, in a dictionary `items` with the key being the menu item name and the value being its ingredients. We append a tuple of the restaurant's info grabbed from Foursquare's API with `items`.

TO BE CONTINUED

### Design Decisions

#### API
We considered many APIs while researching which may be the most helpful for our project. Primarily, we looked into these APIs: Zomato, Nutritionix, OpenMenu, Gipsee, and Foursquare. Initially, Nutritionix seemed to be the most promising API because its demo included listing ingredients for items on a restaurant's menu, which is what we needed. However, upon obtaining an API key, we realized that Nutritionix's data was very lacking in terms of restaurant data overall. Thus we decided to turn to Foursquare, which provided the data we needed about restaurants near a given location, and used it in conjuction with web scraping to access the ingredients of every menu item.

#### Flask
We decided to use Flask because it integrated well with Python and was a more familiar option to the both of us.

#### Web Scraping
Beautiful Soup is a Python package that could parse HTML and XML files, so we integrated it for our web scraping purposes. We decided to use Selenium instead of other libraries like Requests because the sites we were scraping from rendered JavaScript, and only Selenium could handle dynamically loaded webpage content.  We experimented with ChromeDriver before switching to Headless because we did not need a visible browser UI every time we tested our app.

#### Location
Originally, we had desired to include geolocation. However, we soon realized that a user might want to research the best restaurants to go to in an area he/she is unfamiliar with ahead of time, so we chose to allow the user to manually input the location instead.

### User Interface
Our goal in creating the UI was for SafePlates to be easy for the user to read and use, so our design is simple???? TO BE CONTINUED/AXED

### Files
#### Front End
* static
  * `styles.css`: the CSS styling for our web app .
* templates
  * `form.html`: the HTML for our initial form. 
  * `layout.html`: the HTML template `form.html` and `results.html` use.
  * `results.html`: the HTML for our results page, showing a table of restaurant recommendations.

#### Back End
* `app.py`: this file drives our Flask app and includes the logic necessary to run our web app.
* `helpers.py`: this file includes the following helper functions, which are used in `app.py`:
  * `returnSoup(link)`: this function scrapes the web page of the inputted link and returns the HTML of that page.
  * `goodRestaurants(restaurants, user_restrictions)`: this function takes in 2 parameters: an array of restaurants and an array of the user's dietary restrictions. This function filters through the array of restaurants to return an array of only restaurants that satisfy the user's dietary restrictions.
  * `safeFood(item, user_restrictions)`: this function returns whether a menu item is in the user's dietary restrictions.