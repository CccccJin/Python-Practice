import re

dfile = open('mbox-short.txt')
a = input('Plz enter a regular expression: ')
date = dict()
count = 0

for line in dfile:
    line = line.rstrip()
    if re.search(a, line):
        count += 1

print('mobox-short.txt had',count, 'lines that matched',a)
    