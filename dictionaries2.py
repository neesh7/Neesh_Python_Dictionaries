fruit = {"Orange": "a sweet, oranges, citrus fruit",
         "grapes": "a small, sweet fruit, grows in bunches",
         "Mango": "Nice shape,Beautiful, so juicy",
         "lemon": "citrus fruit , so juicy , so sour, women likes lemon",
         "kivy": "it's cute but it's not from  new zeland"
         }
# while True:
#     dict_key = input("please enter a Fruit to look for it's details")
#     if dict_key.casefold() == "quit":
#         break
#     description = fruit.get(dict_key.casefold(), "We don't Have " + dict_key)
#     print(description)

# In order to iterate over a dict
# for snack in fruit:
#     # print(snack)
#     print(fruit[snack])
# we are going to iterate over our dict 10 times and we observe that our order is going to be same.
# for i in range(11):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print("___"*40)

# ordering the Dictionary : we are going to convert our dictionary to a list then we will sort it.
# code1
ordered_keys = list(fruit.keys())
ordered_keys.sort()
for fseq in ordered_keys:
    print(fseq + " _ " + fruit[fseq])
print("#"*80)
# code 2
ordered_keys1 = sorted(list(fruit.keys()))
for fseq2 in ordered_keys1:
    print(fseq2 + " _ " + fruit[fseq2])
print("*"*80)
# code 3
for fseq3 in sorted(fruit.keys()):
    print(fseq3 + " _ " + fruit[fseq3])
    