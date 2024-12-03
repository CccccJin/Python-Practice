fname = input('Enter the file name: ')
fhand = open(fname)
spie = dict()
count = 0

for line in fhand:
    list = line.strip().split()
    for word in list:
        count += 1
        spie[word] = count
        
print(spie)
print('Writing' in spie)