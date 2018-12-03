from flask import Flask, render_template, request
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json

from helpers import returnSoup, goodRestaurants

app = Flask(__name__)

url = 'https://api.foursquare.com/v2/venues/explore'

# browser = webdriver.Chrome()

@app.route("/", methods=["GET"])
def get_form():
    return render_template("form.html")

@app.route("/form", methods=["POST"])
def post_form():
  number_of_recs = 10

  params = dict(
    client_id='F22SZ5OH34NV0ETPBQCJ33UIJGFMDWNMTI0MVUABYPJECIBW',
    client_secret='GTWA3CFSP1Y5PMUNJTWKFOS3QJELCNHRMBOASKL4UDGKYJAK',
    v='20181203',
    suggestedRadius= request.form.get("radius"),
    near=request.form.get("location"),
    query="restaurant",
    limit=number_of_recs
  )

  resp = requests.get(url=url, params=params)
  data = json.loads(resp.text)

  # Pseudocode
  # for each restaurant (WITH URL), scrape menu
  # Store all menu items?
  # Check if menu has items that don't include dietary restriction
  # Store appropriate items
  # Return items

  # Store dietary restrictions from form
  all_restrictions = {
   'vegetarian':set(["meat", "chicken", "beef", "pork", "ham", "wings", "veal", "venison", "ham", "hot dog", "sausage", "steak", "turkey", "lamb"]),
   'soy':set(["soy", "soya", "edamame", "shoyu", "tofu", "tempeh", "miso"]),
   'dairy':set(["milk", "cheese", "cream", "cheddar", "brie", "parmesan", "mozzarella", "butter", "lactose", "pudding", "dairy"]),
   'gluten':set(["gluten", "wheat", "barley", "bread", "roll", "bun", "pizza", "pasta", "rye", "beer", "ale", "lager", "cookie", "crackers"]),
   'peanuts':set(["peanut", "peanuts"]),
   'beef':set(["beef", "steak"]),
   'pork':set(["pork","ham", "bacon","sausage"])}
  user_restrictions = set()
  for checkbox in all_restrictions:
    value = request.form.get(checkbox)
    if value:
        user_restrictions = user_restrictions.union(all_restrictions[checkbox])

  # Access an URL
  restaurants = []
  page = ""
  for i in range(0, number_of_recs):
    try:
      # grabs URL of restaurant if possible
      link = data['response']['groups'][0]['items'][i]['venue']['delivery']['url']

      # parse the html using helper function and store in vcariable `soup`
      soup = returnSoup(link)

      items = {}
      if "grubhub" in link:
        
        for item in soup.find_all("div", attrs={'class':'menuItemNew'}):
          ingredients = item.find_next("p", attrs={'itemprop': 'description'}).text
          name = item.find_next("h6", attrs={'class':'menuItem-name'}).text
          items[ingredients + name] = name 
          #if user_restrictions.isdisjoint(ingredientsSet):
          #   print("hey")
          #   print("You can eat" + item.find_next("h6", attrs={'class':'menuItem-name'}))
          #   try:
          #     restaurants.append(data['response']['groups'][0]['items'][i]['venue'])
          #   except:
          #print(j.text.strip.split)
          # if diet[0] not in i.text.strip.split:
          #   try:
          #     restaurants.append(data['response']['groups'][0]['items'][i]['venue'])
          #   except:
          #     print(i)
      restaurants.append((data['response']['groups'][0]['items'][i]['venue'], items))
      if "seamless" in link:
        print("do something here")
    except:
      print(i)

  # Access address
  # for i in range(0, number_of_recs):
  #   try:
  #     restaurants.append(data['response']['groups'][0]['items'][i]['venue'])
  #   except:
  #     print(i)



  #return json.dumps(data)
  restaurant_recs = goodRestaurants(restaurants, user_restrictions)
  # for item in restaurant_recs:
  #   print(item[0])
  #   print("==========")
  #   print(item[1])
  #   print(len(item))
    
  # return render_template("results.html", results=list(map(lambda x: x[0], restaurants)))
  return render_template("results.html", results=restaurant_recs)


if __name__ == '__main__':
    app.run()