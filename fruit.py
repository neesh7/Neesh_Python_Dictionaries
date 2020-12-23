fruit = {"Orange": "a sweet, oranges, citrus fruit",
         "grapes": "a small, sweet fruit, grows in bunches",
         "Mango": "Nice shape,Beautiful, so juicy",
         "lemon": "citrus fruit , so juicy , so sour, women likes lemon",
         }
print(fruit)
veg = {"Cabbage": "I like cabbage, They are Spicy",
       "Spinach": "i don't like them,They are Good for Eyes",
       "carrot": "Gazar ka Halwa Aaye haye !!!, I like it alot"}
print(veg)
vegies = {"Potato": "Potatoes are acceptable with all kind of sabji",
          "Banana": "it's a fruit but sabji bhi acha hota hai iska",
          "Bhindi": "I like bhindi ka bhujya"}

# Update() method demo
# Suppose i want to join two dictionaries together by that i mean actually updating a dictionary
# we will use update method in order to update our veg dictionaries by using the entries of the vegies
print("_"*80)
veg.update(vegies)
print(veg.update(vegies)) # This will return NONE as It doesn't returns any new dict it just updates old one.
print(veg)
# Copy() Method demo
# we use copy method to genrate a new dictionary by copying entries of old one so that the old one remains unchanged
print("________________________________________")
Veg2 = veg.copy()
print(Veg2)