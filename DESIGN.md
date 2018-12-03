# Safeplates
2018 Harvard CS50 Final Project: Catherine Yeo and Hannah Cole

## Design

### Summary: How does Safeplates work?
This web app is built and hosted locally, coded in Python and HTML/CSS. It uses [Foursquare](https://developer.foursquare.com/)'s API to provide restaurant data based on location and radius. That data includes links to restaurant menus on [Seamless](https://www.seamless.com/) and [GrubHub](https://www.grubhub.com/). After we have accessed the restaurant data from the API's data in a JSON format, we scrape the restaurant's online menu to access all menu items and their ingredients. We then parse through all the ingredients and return food items (and the restaurants they're from) that adhere to the user's dietary restrictions. 

### Detailed Walkthrough

### User Interface