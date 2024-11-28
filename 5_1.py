# Once “done” is entered, print out the total, count, and average of the integers. 
# If the user enters anything other than a integers, detect their mistake using try and except and print an error message and skip to the next integers.

total = 0
count = 0

while True:
    a = input("enter a number: ")
    if a == 'done':
        print(count,total,average)
        break
    try:
        conver_to_int = float(a)
        total = conver_to_int + total
        count = count +1
        # sum = sum + a
        average = float(total/count)
        print(count,total,average)
    except:
        if a is not int:
            print("Please enter integer")
  

    
    