# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. 
# Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, 
# print out the average spam confidence.

fname = input('Enter the file name: ')
fhand = open(fname)

# for line in fhand:
#    if line.isupper():
#        print(line)
count = 0
sum = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        a = line.find(':')
        b = float(line[a+1:])
        print('confidence: ',b)
        count = count + 1
        print('Confidence number: ',count)
        sum += b
        print('Sum: ',sum)
        average = sum/count
        print('Average: ',average)
        
        




   



