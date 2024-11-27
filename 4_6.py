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

a = float(hour)
b = float(rate)

def computepay(a,b):
    x = (a-40)*1.5 * b + 40 * b
    return x

if a <= 40:
    result = a * b
elif a > 40:
    result = computepay(a,b)
print("result = ", result)
