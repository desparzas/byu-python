# Prompt the user for their first name. Then, prompt them for their last name. Display the text back all on one line saying, "Your name is last-name, first-name, last-name" as shown:

# Ask the user for their first name
first_name = input("What is your first name? ")

# Ask the user for their last name
last_name = input("What is your last name? ")

# Display the user's full name, using fstring
print(f"Your name is {last_name}, {first_name}, {last_name}")