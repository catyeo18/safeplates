from flask import Flask, render_template, request
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json

from helpers import returnSoup, goodRestaurants

app = Flask(__name__)

url = 'https://api.foursquare.com/v2/venues/explore'

@app.route("/", methods=["GET"])
def get_form():
    return render_template("form.html")

@app.route("/form", methods=["POST"])
def post_form():
  number_of_recs = 20

  # Access data from FourSquare's API
  params = dict(
    client_id='F22SZ5OH34NV0ETPBQCJ33UIJGFMDWNMTI0MVUABYPJECIBW',
    client_secret='GTWA3CFSP1Y5PMUNJTWKFOS3QJELCNHRMBOASKL4UDGKYJAK',
    v='20181203',
    suggestedRadius= request.form.get("radius"),
    near=request.form.get("location"),
    query="restaurant",
    limit=number_of_recs
  )

  # Load data into JSON
  resp = requests.get(url=url, params=params)
  data = json.loads(resp.text)

  # Dictionary of deitary restrictions
  all_restrictions = {
   'vegetarian':set(["meat", "chicken", "beef", "pork", "ham", "wings", "veal", "venison", "ham", "hot dog", "sausage", "steak", "turkey", "lamb", "pastrami", "salami", "shrimp", "fish", "seafood", "clam", "octopus", "squid", "mussel", "tuna", "salmon", "swordfish", "pepperoni", "prosciutto", "pancetta", "b.l.t", "blt", "anchovy", "anchovies", "burger", "carne", "carnitas", "barbacoa", "scallop", "lengua", "al pastor", "oyster", "pig", "intestine", "eel"]),
   'soy':set(["soy", "soya", "edamame", "shoyu", "tofu", "tempeh", "miso"]),
   'dairy':set(["milk", "cheese", "cream", "queso", "cheddar", "cheesy", "swiss", "creamy", "brie", "parmesan", "mozzarella", "pizza", "calzone", "butter", "lactose", "pudding", "dairy", "yogurt", "yoghurt"]),
   'gluten':set(["gluten", "wheat", "barley", "bread", "roll", "bun", "pizza", "ramen", "soba", "udon", "pasta", "rye", "beer", "ale", "lager", "cookie", "crackers", "sub", "wrap", "calzone", "cake", "toast", "sandwich", "pita", "soy sauce", "tortellini", "ravioli", "flour", "spaghetti", "linguine", "fettuccine", "penne", "panini"]),
   'peanuts':set(["peanut", "peanuts"]),
   'beef':set(["beef", "steak", "pastrami", "salami", "pepperoni", "prosciutto", "pancetta", "b.l.t", "blt"]),
   'pork':set(["pork", "ham", "bacon", "sausage", "pepperoni", "salami"])}
  
  # Store dietary restrictions from form in a set
  user_restrictions = set()
  for checkbox in all_restrictions:
    value = request.form.get(checkbox)
    if value:
        user_restrictions = user_restrictions.union(all_restrictions[checkbox])

  # Variable to store all restaurants in an array
  restaurants = []
  
  # Iterate through restaurants
  for i in range(0, number_of_recs):
    try:
      # Grabs URL of restaurant if possible
      link = data['response']['groups'][0]['items'][i]['venue']['delivery']['url']

      # Parse the HTML using helper function and store in variable `soup`
      soup = returnSoup(link)

      items = {}
      # Scrabe from Grubhub or Seamless
      if "grubhub" in link or "seamless" in link:
        
        # Find item in the web page based on their HTML tags/attributes
        for itemName in soup.find_all("h6", attrs={'class':'menuItem-name'}):
          ingredients = itemName.find_next("p", attrs={'itemprop': 'description'}).text
          items[ingredients + itemName.text] = itemName.text
          
      # Add data to the restaurants array
      restaurants.append((data['response']['groups'][0]['items'][i]['venue'], items))

    except:
      pass

  # Call helper function to filter through which restaurants have items that satisfy 
  # user's dietary restrictions
  restaurant_recs = goodRestaurants(restaurants, user_restrictions)
  return render_template("results.html", results=restaurant_recs)


if __name__ == '__main__':
    app.run()