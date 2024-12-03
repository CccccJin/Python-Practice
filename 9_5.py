# This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). 
# At the end of the program, print out the contents of your dictionary.
# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

ofile = input('Enter a file name:')
dfile = open(ofile)

largest = None
minimum = None
lit = dict()

for line in dfile:
    if line.startswith('From '):
        try:
            words = line.rstrip().split()
            #print(words)
            #atdop = words[1].split('@')
            #print(atdop)
            word = words[1]
            #print(word)
            lit[word] = lit.get(word,0) +1
            #print(lit[word])
            if largest is None or lit[word] > largest:
                largest = lit[word]
            if minimum is None or lit[word] < minimum:
                minimum = lit[word]
        except IndexError:
            pass

max_address = None
max_count = 0
for email, count in lit.items():  # Iterate through the dictionary
    if count > max_count:
        max_address = email
        max_count = count

print(max_address, max_count)






    

