# Once “done” is entered, print out the total, count, and average of the integers. 
# If the user enters anything other than a integers, detect their mistake using try and except 
# and print an error message and skip to the next integers.
# Write another program that prompts for a list of numbers as above 
# and at the end prints out both the maximum and minimum of the numbers instead of the average.

total = 0
count = 0
largest = None
minimum = None

while True:
    a = input("enter a number: ")
    if a == 'done':
        print(count,total,largest,minimum)
        break
    try:
        conver_to_int = float(a)
        total = conver_to_int + total
        count = count +1
        # sum = sum + a
        average = float(total/count)
        if largest is None or conver_to_int > largest:
            largest = conver_to_int
        if minimum is None or conver_to_int < minimum:
            minimum = conver_to_int
        print(count,total,largest,minimum)
    except:
        if a is not int:
            print("Please enter integer")
  

    
    
