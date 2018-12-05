# Safeplates
2018 Harvard CS50 Final Project: Catherine Yeo and Hannah Cole

## What Is Safeplates?
For individuals who have specific dietary restrictions, it is often difficult to find restaurants to go to that have available menu options that satisfy those restrictions. We created Safeplates to solve that problem.

**Safeplates** is a web app that gives local restaurant recommendations based on the dietary restrictions a user inputs. For example, if Alice can’t eat soy, the app would parse the menus of an inputted region's restaurants (of a specified radius) to determine which restaurants have the most soy-free options. 

## How To Configure Safeplates

Note: Please ensure you have Python and all the associated libraries used in this webapp (detailed more in DESIGN.md) installed.

### Step 1: 
Clone this repository locally. 

### Step 2:
In Terminal, enter the directory to which this repository is cloned. 
Then, enter the directory `safeplates`.

### Step 3:
In Terminal, type `flask run`. You should see something like this: 

```
* Environment: production 
WARNING: Do not use the development server in a production environment.
Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://80.0.0.1:5000/ (Press CTRL+C to quit) 
```

### Step 4:
Open the browser linked in the above Terminal message. In the example above, you would go to the URL `http://80.0.0.1:5000/`.

## How To Use Safeplates

### Step 1:
Check all the dietary restrictions that apply to you.

### Step 2:
Enter the location of where you would like to find restaurants. You could enter an address, city, or zip code. 

### Step 3:
Enter your preferred radius of how close the suggested restaurants are to your inputted location.

### Step 4: 
Submit the form!

