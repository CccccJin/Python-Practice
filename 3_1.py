# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

hour = int(input("Enter hour = "))
rate = int(input("Enter rate = "))
#a = int(hour)
#b = int(rate)
if hour <= 40:
    result = hour * rate
elif hour > 40:
    result = (hour-40)*1.5 * rate + 40 * rate
print("result = ",result)
