# Individual Github Exercise
from feature_2 import*

# Prints text asking for number of user input
user_str = input("Enter a string: ")

words = [word.lower() for word in user_str.split()]
sort_string(words)

print("The sorted words are:")
for word in words:
    print(word)
