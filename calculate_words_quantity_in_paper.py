ofile = input('Enter a file name: ')
dfile = open(ofile)

date = dict()
largest = None
minimum = None

for line in dfile:
        try:
            words = line.rstrip().split()
            for stime in words:
                date[stime] = date.get(stime,0) +1
        except IndexError:
            pass

lit = list()

for k,v in list(date.items()):
    lit.append((v,k))

lit.sort(reverse=True)

for k,v in lit[:100]:
    print(v,k)