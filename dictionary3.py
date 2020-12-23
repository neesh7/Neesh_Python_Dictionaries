# like key method we can also use value method in order to get a list of values
fruit = {"Orange": "a sweet, oranges, citrus fruit",
         "grapes": "a small, sweet fruit, grows in bunches",
         "Mango": "Nice shape,Beautiful, so juicy",
         "lemon": "citrus fruit , so juicy , so sour, women likes lemon",
         "kivy": "it's cute but it's not from  new zeland"
         }
for val in fruit.values():
    print(val)
    # it prints  the list of values but it is not advisable we can do it much efficiently by using key method.
print("_________________________________________")
for key in fruit:
    print(fruit[key])

# we can do other basic things like
print(fruit.keys())
print(fruit.values())
# both of these line  of code will return list of keys and values i.e.., dict_keys and dict_values
# and both together is called view objects
fruit_keys = fruit.keys()
print(fruit_keys)
fruit["tomato"] = "not nice to eat with ice cream"
print(fruit_keys)
print("__"*80)
print(fruit)
print(fruit.items())
# Extracting tuple from this fruit.items
print("#"*80)
f_tuples = tuple(fruit)  # This will give  only tuple of our keys
print(f_tuples)
f_tuples1 = tuple(fruit.items())  # This will give our tuple of keys and values altogether called as view object.
print(f_tuples1)
# iterating over tuples
print("#"*80)
for snack in f_tuples1:
    items, description = snack
    print(items + " is " + description)
