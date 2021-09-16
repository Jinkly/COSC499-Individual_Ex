# Individual Github Exercise
from feature_1 import*

# Prints text asking for number of user input
num = int(input("Enter number of elements : "))

# Read inputs from user using map() function
user_input = list(map(int, input("\nEnter the numbers : ").strip().split()))[:num]

sort_int(user_input)
print("\nList is - ", user_input)