
total_cost = 0 # This variable stores the total cost of the purchase.
# At the beginning, the value is 0.


# The try block is used to detect possible errors
# when the user enters incorrect data.
try:

    # The program asks the user to enter the product name.
    # input() saves the value as text.
    product_name = input("  Please, enter the produt name:  ")

    # The program asks for the product price.
    priece = float(input("  Please, enter the product priece:  "))

    # The program asks for the quantity of products.
    count = int(input("  Please, enter the count:  "))

# If the user enters a wrong value (like letters instead of numbers),
# Python generates a ValueError and this message appears.
except ValueError:
      print("Error, input the correct value")
    

# Here the program calculates the total cost.
# It multiplies the price by the quantity.
total_cost = priece * count


print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

# The program prints the product information.

print(f"|Product name: {product_name}| \n |Priece: ${priece}| \n |count: {count}| \n |Total cost: {total_cost}|")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

'''This program records store sales
The user enters the product name, price, and quantity.
 The program calculates the total cost and shows a summary.'''