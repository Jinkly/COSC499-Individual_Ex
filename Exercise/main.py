# Individual Github Exercise

# Function that sorts words form a string provided by the user alphabetically
def sort_string(user_words):

    # sort the list
    user_words.sort()
    return user_words


# Prints text asking for number of user input
user_str = input("Enter a string: ")

words = [word.lower() for word in user_str.split()]
sort_string(words)

print("The sorted words are:")
for word in words:
    print(word)
