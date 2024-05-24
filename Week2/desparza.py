# I added error handling and loops, to prevent that the code crashes if the user inputs a string,
# and to validate that the program only continues when the input it's correct,
# in most cases is when the input is a number, and the number is greater than 0. 
# But with the sales tax, the number must be greater than 0 and less than or equal to 100.
# Also, the payment amount must be greater than or equal to the total.
# I also limited the number of decimal before the zero to 2
# :)

while True:
    try:
        child_meal_price = input("What is the price of a child's meal?: ")
        child_meal_price = float(child_meal_price)
        if child_meal_price <= 0:
            print("The price of a child's meal must be greater than 0")
        else:
            break
    except ValueError:
        print("Please enter a valid number")

while True:
    try:
        adult_meal_price = input("What is the price of an adult's meal?: ")
        adult_meal_price = float(adult_meal_price)
        if adult_meal_price <= 0:
            print("The price of an adult's meal must be greater than 0")
        else:
            break
    except ValueError:
        print("Please enter a valid number")


while True:
    try:
        number_of_children = input("How many children are there?: ")
        number_of_children = int(number_of_children)
        if number_of_children <= 0:
            print("The number of children must be greater than 0")
        else:
            break
    except ValueError:
        print("Please enter a valid number")

while True:
    try:
        number_of_adults = input("How many adults are there?: ")
        number_of_adults = int(number_of_adults)
        if number_of_adults <= 0:
            print("The number of adults must be greater than 0")
        else:
            break
    except ValueError:
        print("Please enter a valid number")

subtotal = (child_meal_price * number_of_children) + (adult_meal_price * number_of_adults)

print(f"Subtotal: ${subtotal:.2f}")

while True:
    try:
        sales_tax = input("What is the sales tax rate?: ")
        sales_tax = float(sales_tax)
        if sales_tax <= 0 or sales_tax > 100:
            print("The sales tax rate must be greater than 0 and less than or equal to 100")
        else:
            break
        sales_tax = sales_tax / 100
    except ValueError:
        print("Please enter a valid number")

sub_total_tax = subtotal * sales_tax
print(f"Sales tax: ${sub_total_tax:.2f}")

total = subtotal + sub_total_tax

print(f"Total: ${total:.2f}")


while True:
    try:
        payment_amount = input("What is the payment amount?: ")
        payment_amount = float(payment_amount)
        if payment_amount < total:
            print("The payment amount must be greater than or equal to the total")
        else:
            break
    except ValueError:
        print("Please enter a valid number")

change = payment_amount - total
print(f"Change: ${change:.2f}")




