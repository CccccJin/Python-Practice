import re

ofile = input('Enter a file:')
dfile = open(ofile)
#dfile = open('mbox-short.txt')
count = 0
summ = 0

for line in dfile:
    line = line.strip()
    x = re.findall('^New.*: ([0-9][0-9][0-9][0-9][0-9])',line)
    if len(x)>0:
        for num in x:
            summ = summ + int(num)
            count += 1

#print(count,y)
print(int(summ/count))