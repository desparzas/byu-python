array = []
print("Enter a list of numbers, type 0 when finished.")
value = None 

# Have the user enter both positive and negative numbers, then find the smallest positive number (the positive number that is closest to zero).

# Sort the numbers in the list and display the new, sorted list. Hint: There are python libraries that can help you here, try searching the internet for them.

while value != 0:
    value = int(input("Enter a number"))
    if value !=0:
        array.append(value)
# sum
# average = sum / size
# largest x
if len(array)>0:
    max = array[0]
    min = array[0]
    sum = 0
    n = len(array)

    for value in array: # iterating the values
        if value > max: # asking
            max = value
        
        if value < min:
            min = value 
        sum += value 
    
    avg = sum/n


    print(array)
    print("MAX: ", max)
    print("SUM: ", sum)
    print("AVERAGE: ", avg)
    print("MIN: ", min)
