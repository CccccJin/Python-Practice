# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input


hour = input("Enter hour = ")
try:
    diu = float(hour)
except:
    print("Error, please enter numeric input") 
    quit()
    
rate = input("Enter rate = ")
try:
    check1 = float(rate)
except:
    print("Error, please enter numeric input")
    quit()
    
a = int(hour)
b = int(rate)

if a <= 40:
    result = a * b
elif a > 40:
    result = (a-40)*1.5 * b + 40 * b
print("result = ",result)
