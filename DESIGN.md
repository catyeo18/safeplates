# Safeplates
2018 Harvard CS50 Final Project: Catherine Yeo and Hannah Cole


**Safeplates** is a web app that gives local restaurant recommendations based on the dietary restrictions a user inputs.

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
The user begins by going to the form to which he/she can input dietary restrictions, location, and preferred radius.

### Design Decisions

#### Flask

#### Web Scraping
We decided to use Selenium instead of other web scraping libraries like Requests because the sites we were scraping from rendered JavaScript, and only Selenium could handle dynamically loaded webpage content.

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