# Create a program that takes some text and returns a list of all the characters
# in the text that are not vowels , sorted in alphabetical order
sample_text = "Python is powerful"
vowels= frozenset("aeiou")
finalset= set(sample_text).difference(vowels)
print(finalset)
print("="*80)
print("Sorted output is")
finalList = sorted(finalset)
print(finalList)