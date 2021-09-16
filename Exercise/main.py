# Prints text asking for number of user input
n = int(input("Enter number of elements : "))

# Read inputs from user using map() function
user_input = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]

print("\nList is - ", user_input)