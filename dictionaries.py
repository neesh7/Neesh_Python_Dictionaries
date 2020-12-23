# Declaring Dictionaries
fruit = {"Orange": "a sweet, oranges, citrus fruit",
         "grapes": "a small, sweet fruit, grows in bunches",
         "Mango": "Nice shape,Beautiful, so juicy",
         "lemon": "citrus fruit , so juicy , so sour, women likes lemon",
         # "Mango": "Duplicating same Entries two times does'nt help"
         }
# code 1 :
print(fruit)
#    # Accessing items(Values) in Dictionaries using their key name
print(fruit["Orange"])
#   # Adding new Entry to Dictionaries
fruit["Lime"] = "great with tequila"
print(fruit)
fruit["Pear"] = "an odd shaped apple"
print(fruit)
#   # Updating or overwriting old entries
fruit["Pear"] = "an beautiful and juicy fruit"
print(fruit)
#   # Deleting Dictionaries content
del fruit["Pear"]  # pear is being deleted from the dictionaries called fruit
print(fruit)
# del fruit
# print(fruit)  # this line causes an error as dictionaries does'nt exist anymore
# clearing whole dict items at once
# fruit.clear()
# print(fruit)
# Asking for an item which doest exist in the dict will cause an error
# print("Asking for an item which doest exist in the dict will cause an error\n As for example")
# print(fruit["Tomato"])  # cz a key with name Tomato doesnt exit in the dictionaries so what we do is simply fix it

############### code2:
# while True:
#     dict_key= input("please enter a Fruit to look for it's details")
#     if dict_key.casefold() == "quit":
#         break
#     description = fruit.get(dict_key.casefold())
#     print(description)
# Code 3
while True:
    dict_key = input("please enter a Fruit to look for it's details")
    if dict_key.casefold() == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("We don't Have " + dict_key)
