# Individual Github Exercise
from feature_1 import*
from feature_2 import*

# Prompts the user to enter 0 or 1
choice = int(input("Enter 0 or 1: "))

# If user enters 0, feature 1 is run
if choice == 0:
    # Prints text asking for number of user input
    num = int(input("Enter number of elements : "))

    # Read inputs from user using map() function
    user_input = list(map(int, input("\nEnter the numbers : ").strip().split()))[:num]

    sort_int(user_input)
    print("\nList is - ", user_input)

# If user enters 1, feature 2 is run
elif choice == 1:
    # Prints text asking for number of user input
    user_str = input("Enter a string: ")

    words = [word.lower() for word in user_str.split()]
    sort_string(words)

    print("The sorted words are:")
    for word in words:
        print(word)

# If neither 0 or 1 is entered, a message is printed
else:
    print("Restart program right now and enter 0 or 1!")
