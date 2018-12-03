from flask import Flask, render_template, request
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json

from helpers import returnSoup

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
    v='20181118',
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
  all_restrictions = ['vegetarian', 'soy', 'dairy', 'gluten', 'peanuts', 'beef', 'pork']
  user_restrictions = []
  for checkbox in all_restrictions:
    value = request.form.get(checkbox)
    if value:
        user_restrictions.append(checkbox)

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
          items[ingredients] = name 
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
        for item in items:
          print(items[item])
      if "seamless" in link:
        print("do something here")
    except:
      print(i)



  restaurants = []
  # Access address
  for i in range(0, number_of_recs):
    try:
      restaurants.append(data['response']['groups'][0]['items'][i]['venue'])
    except:
      print(i)



  #return json.dumps(data)
  return render_template("results.html", results=restaurants)


if __name__ == '__main__':
    app.run()