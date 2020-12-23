my_list = ["a", "b", "c", "d"]
# print(my_list)
# new_string = " "
# for c in my_list:
#     new_string += c + " , "
# print(my_list)
# using join method in order to concanate string into a single sequence
print("#"*80)
new_string1 = " , ".join(my_list)
print(new_string1)
# using join method we can concenate any type of string just providing a seprator to it
letters = "abcdefghijklmnopqrstuvwxyz"
# printing letters in a single sequence using join method and comma as an seprators
print(letters)
neil = ", ".join(letters)
print(neil)
# also
num= "123456789"
print("Fish, ".join(num))

