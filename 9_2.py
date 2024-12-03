# Write a program that categorizes each mail message by which day of the week the commit was done. 
# To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. 
# At the end of the program print out the contents of your dictionary (order does not matter).
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

ofile = input('Enter a file name: ')
dfile = open(ofile)

date = dict()
#count = 0
#counts_word = 0
largest = None
minimum = None

for line in dfile:
    if line.startswith('From'):
        try:
            words = line.rstrip().split()
            for word in words[1:2]:
                date[word] = date.get(word,0) +1
                if largest is None or date[word] > largest:
                    largest = date[word]
                if minimum is None or date[word] < minimum:
                    minimum = date[word]
        except IndexError:
            pass

lst = list(date.values())
lst.sort()
print(lst)
if 'cwen@iupui.edu' in date:
    print('cwen@iupui.edu', int(int(date['cwen@iupui.edu'])/2))

#mbox-short.txt



