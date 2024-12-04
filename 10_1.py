ofile = input('Enter a file name: ')
dfile = open(ofile)

date = dict()
largest = None
minimum = None

for line in dfile:
    if line.startswith('From '):
        try:
            words = line.rstrip().split()
            for word in words[1:2]:
                date[word] = date.get(word,0) +1
        except IndexError:
            pass

lit = list()
for k,v in list(date.items()):
    lit.append((v,k))


lit.sort(reverse=True)
for k,v in lit[:1]:
    print(v,k)