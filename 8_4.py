fname = input('Enter the file name: ')
fhand = open(fname)

list = list[:]
sumeee = []

for line in fhand:
    list = line.split()
    for word in list:
        if word not in sumeee:
            sumeee.append(word)
            #return sumeee      

sumeee.sort()
    
print(sumeee)

