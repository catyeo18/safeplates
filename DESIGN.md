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
* BeautifulSoup (for web scraping)

#### Front End
* HTML
* CSS
* Javascript
* Jinja

### Detailed Walkthrough
The user begins by going to the form to which he/she can input dietary restrictions, location, and preferred radius. The dietary restrictions are selected through a list of checkboxes, so the user can check all that apply. The location input can take in an address, city, and/or zip code. 

Then, the user clicks the 'Submit' button to submit the form. Once that happens, the web app uses the inputted location and radius to access a list of restaurants given by Foursquare's API in JSON. The API provides us with information like name, cuisine, address, menu link, etc. It also stores the user's dietary restrictions in a set.

We iterate through that list of restaurants to look for the URLs of the restaurants' menus. Once the URL is found, the HTML is parsed and returned using the helper function `returnSoup` in `helpers.py`, which utilizes BeautifulSoup, Headless, and Selenium to scrape the webpage. Now, we look for specific HTML tags/attributes within that block of scraped HTML. Every menu item is embedded within HTML tags with class `menuItem-name`, so we iterate through the menu items to store its ingredients, which all have `itemprop` labelled with `description`, in a dictionary `items` with the key being the menu item name and the value being its ingredients. We append a tuple of the restaurant's info grabbed from Foursquare's API with `items`.

### Design Decisions

#### API

#### Flask

#### Web Scraping
We decided to use Selenium instead of other web scraping libraries like Requests because the sites we were scraping from rendered JavaScript, and only Selenium could handle dynamically loaded webpage content.

#### Location
Originally, we had desired to include geolocation. BUT tbc

### User Interface

### Files
#### Front End
* static
  * `styles.css`: the CSS styling for our web app 
* templates
  * `form.html`: 
  * `layout.html`: 
  * `results.html`: 

#### Back End
* `app.py`: this file drives our Flask app and includes the logic necessary to run our web app.
* `helpers.py`: this file includes the following helper functions, which are used in `app.py`:
  * `returnSoup(link)`: this function scrapes the web page of the inputted link and returns the HTML of that page.
  * `goodRestaurants(restaurants, user_restrictions)`: